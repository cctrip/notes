---
bookCollapseSection: false
weight: 1
title: "Service通信"
---

# Service通信

在Kubernetes中，service是一种抽象，定义了Pod的逻辑集和访问它们的策略（有时将此模式称为微服务）。service所针对的Pod集合通常由selector确定。https://kubernetes.io/docs/concepts/services-networking/service/

***

## Service服务发现

如果您可以使用Kubernetes API在应用程序中发现service，则可以查询API服务器以获取endpoint，只要service中的Pod集合发生更改，endpoint就会更新。

对于非本机应用程序，Kubernetes提供了在应用程序和后端Pod之间放置网络端口或负载平衡器的方法。

***

## Service资源定义

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: MyApp
  ports:
    - protocol: TCP
      port: 80
      targetPort: 9376
```

***

## 实现

Kubernetes集群中的每个节点都运行一个kube-proxy。 kube-proxy负责为service实现一种VIP(cluster ip)

目前官方的proxy模式有三种

### userspace

![](userspace.svg)



此模式下，由kube-proxy随机选取port进行监听，并创建iptables规则，将所有到达cluster ip的数据转发到kube-proxy监听的端口上，由kube-proxy通过SessionAffinity配置来确定发送给哪个pod

***

### iptables

![](iptables.svg)

此模式下，kube-proxy针对每个service创建iptables规则，所有流量都通过iptables规则和路由表处理流量转发

```markdown
# 以aws为例,cluster ip为10.100.254.226，endpoint为172.31.178.122:80,172.31.178.161:80,172.31.179.80:80,nodeport为30028

# pod or node --> cluster ip --> endpoint
*nat
-A PREROUTING -m comment --comment "kubernetes service portals" -j KUBE-SERVICES #pod所有流量先进入KUBE-SERVICES检查
-A OUTPUT -m comment --comment "kubernetes service portals" -j KUBE-SERVICES  #node流量通过OUTPUT进入KUBE-SERVICES
-A KUBE-SERVICES -d 10.100.254.226/32 -p tcp -m comment --comment "ops-test/nginx-service: cluster IP" -m tcp --dport 80 -j KUBE-SVC-473SUSYUDXM6XRRH    #匹配目的ip为10.100.254.226
#随机选择后端
-A KUBE-SVC-473SUSYUDXM6XRRH -m statistic --mode random --probability 0.33333333349 -j KUBE-SEP-WWIE6AZWAXCTMCNN
-A KUBE-SVC-473SUSYUDXM6XRRH -m statistic --mode random --probability 0.50000000000 -j KUBE-SEP-ZBMAWDEBUXPXQHDH
-A KUBE-SVC-473SUSYUDXM6XRRH -j KUBE-SEP-VPHXZB6KBMWRSLML
#将目标地址转换为172.31.178.243:9300
-A KUBE-SEP-VPHXZB6KBMWRSLML -s 172.31.179.80/32 -j KUBE-MARK-MASQ
-A KUBE-SEP-VPHXZB6KBMWRSLML -p tcp -m tcp -j DNAT --to-destination 172.31.179.80:80

通过路由规则找对应的pod(pod到pod间通信)

# endpoint --> cluster ip --> pod or node
回来的包经过conntrack模块直接做SNAT操作


# externel --> nodeport --> endpoint
*nat
-A PREROUTING -m comment --comment "kubernetes service portals" -j KUBE-SERVICES #外部所有流量先进入KUBE-SERVICES检查
-A KUBE-SERVICES -m comment --comment "kubernetes service nodeports; NOTE: this must be the last rule in this chain" -m addrtype --dst-type LOCAL -j KUBE-NODEPORTS   #KUBE-SERVICES最后一条进入KUBE-NODEPORTS
-A KUBE-NODEPORTS -p tcp -m comment --comment "ops-test/nginx-service:" -m tcp --dport 30028 -j KUBE-MARK-MASQ #打标
-A KUBE-NODEPORTS -p tcp -m comment --comment "ops-test/nginx-service:" -m tcp --dport 30028 -j KUBE-SVC-473SUSYUDXM6XRRH  #后续的DNAT跟cluster ip类似

# endpoint --> nodeport
回来的包经过conntrack模块直接做SNAT操作，转换成nodeport

# nodeport --> externel
-A KUBE-POSTROUTING -m comment --comment "kubernetes service traffic requiring SNAT" -m mark --mark 0x4000/0x4000 -j MASQUERADE --random-fully   #跟外部交互需要做SNAT
```

***

### ipvs

![](ipvs.svg)



在 `ipvs` 模式下，kube-proxy监视Kubernetes服务和端点，调用 `netlink` 接口相应地创建 IPVS 规则， 并定期将 IPVS 规则与 Kubernetes 服务和端点同步。 该控制循环可确保IPVS 状态与所需状态匹配。访问服务时，IPVS 将流量定向到后端Pod之一。

IPVS代理模式基于类似于 iptables 模式的 netfilter 挂钩函数， 但是使用哈希表作为基础数据结构，并且在内核空间中工作。 这意味着，与 iptables 模式下的 kube-proxy 相比，IPVS 模式下的 kube-proxy 重定向通信的延迟要短，并且在同步代理规则时具有更好的性能。 与其他代理模式相比，IPVS 模式还支持更高的网络流量吞吐量。

IPVS提供了更多选项来平衡后端Pod的流量。 这些是：

- `rr`: round-robin
- `lc`: least connection (smallest number of open connections)
- `dh`: destination hashing
- `sh`: source hashing
- `sed`: shortest expected delay
- `nq`: never queue



```markdown
# pod or node --> cluster ip --> endpoint
-A PREROUTING -m comment --comment "kubernetes service portals" -j KUBE-SERVICES
-A OUTPUT -m comment --comment "kubernetes service portals" -j KUBE-SERVICES
-A KUBE-SERVICES -m set --match-set KUBE-CLUSTER-IP dst,dst -j ACCEPT

ipvs处理dnat，进入POSTROUTING链
# endpoint --> cluster ip --> pod or node
回来的包经过conntrack模块直接做SNAT操作


# externel --> nodeport --> endpoint
*nat
-A PREROUTING -m comment --comment "kubernetes service portals" -j KUBE-SERVICES
-A KUBE-SERVICES -m addrtype --dst-type LOCAL -j KUBE-NODE-PORT
-A KUBE-NODE-PORT -p tcp -m comment --comment "Kubernetes nodeport TCP port with externalTrafficPolicy=local" -m set --match-set KUBE-NODE-PORT-LOCAL-TCP dst -j RETURN
-A KUBE-NODE-PORT -p tcp -m comment --comment "Kubernetes nodeport TCP port for masquerade purpose" -m set --match-set KUBE-NODE-PORT-TCP dst -j KUBE-MARK-MASQ

ipvs处理dnat，进入POSTROUTING链
# endpoint --> nodeport
回来的包经过conntrack模块直接做SNAT操作，转换成nodeport

-A POSTROUTING -m comment --comment "kubernetes postrouting rules" -j KUBE-POSTROUTING
-A POSTROUTING -s 169.254.123.0/24 ! -o docker0 -j MASQUERADE
-A KUBE-POSTROUTING -m comment --comment "kubernetes service traffic requiring SNAT" -m mark --mark 0x4000/0x4000 -j MASQUERADE
-A KUBE-POSTROUTING -m comment --comment "Kubernetes endpoints dst ip:port, source ip for solving hairpin purpose" -m set --match-set KUBE-LOOP-BACK dst,dst,src -j MASQUERADE
```



ipvs 会使用 iptables 进行包过滤、SNAT、masquared(伪装)。具体来说，ipvs 将使用`ipset`来存储需要`DROP`或`masquared`的流量的源或目标地址，以确保 iptables 规则的数量是恒定的，这样我们就不需要关心我们有多少服务了

下表就是 ipvs 使用的 ipset 集合：

| set name                       | members                                                      | usage                                                        |
| :----------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| KUBE-CLUSTER-IP                | All service IP + port                                        | Mark-Masq for cases that `masquerade-all=true` or `clusterCIDR` specified |
| KUBE-LOOP-BACK                 | All service IP + port + IP                                   | masquerade for solving hairpin purpose                       |
| KUBE-EXTERNAL-IP               | service external IP + port                                   | masquerade for packages to external IPs                      |
| KUBE-LOAD-BALANCER             | load balancer ingress IP + port                              | masquerade for packages to load balancer type service        |
| KUBE-LOAD-BALANCER-LOCAL       | LB ingress IP + port with `externalTrafficPolicy=local`      | accept packages to load balancer with `externalTrafficPolicy=local` |
| KUBE-LOAD-BALANCER-FW          | load balancer ingress IP + port with `loadBalancerSourceRanges` | package filter for load balancer with `loadBalancerSourceRanges` specified |
| KUBE-LOAD-BALANCER-SOURCE-CIDR | load balancer ingress IP + port + source CIDR                | package filter for load balancer with `loadBalancerSourceRanges` specified |
| KUBE-NODE-PORT-TCP             | nodeport type service TCP port                               | masquerade for packets to nodePort(TCP)                      |
| KUBE-NODE-PORT-LOCAL-TCP       | nodeport type service TCP port with `externalTrafficPolicy=local` | accept packages to nodeport service with `externalTrafficPolicy=local` |
| KUBE-NODE-PORT-UDP             | nodeport type service UDP port                               | masquerade for packets to nodePort(UDP)                      |
| KUBE-NODE-PORT-LOCAL-UDP       | nodeport type service UDP port with `externalTrafficPolicy=local` | accept packages to nodeport service with `externalTrafficPolicy=local` |

***

### ipvs-ebpf

