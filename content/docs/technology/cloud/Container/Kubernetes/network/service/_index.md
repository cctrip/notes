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
# 以aws为例,cluster ip为10.100.14.55，endpoint为172.31.177.209:9300,172.31.178.228:9300,172.31.178.243:9300

# pod --> cluster ip or nodeip + nodeport
*nat
-A PREROUTING -m comment --comment "kubernetes service portals" -j KUBE-SERVICES #所有流量先进入KUBE-SERVICES检查
-A KUBE-SERVICES -d 10.100.14.55/32 -p tcp -m comment --comment "efk-logs/elasticsearch-master:transport cluster IP" -m tcp --dport 9300 -j KUBE-SVC-5X4DO3E4TUEJQMU2   #匹配目的ip为10.100.14.55
#随机选择后端
-A KUBE-SVC-5X4DO3E4TUEJQMU2 -m statistic --mode random --probability 0.33333333349 -j KUBE-SEP-YUFQX2WIG47HGIFG
-A KUBE-SVC-5X4DO3E4TUEJQMU2 -m statistic --mode random --probability 0.50000000000 -j KUBE-SEP-5NAUVOHACN3LRMPO
-A KUBE-SVC-5X4DO3E4TUEJQMU2 -j KUBE-SEP-JBFAMRDVQ5CON62O
#将目标地址转换为172.31.178.243:9300
-A KUBE-SEP-JBFAMRDVQ5CON62O -s 172.31.178.243/32 -j KUBE-MARK-MASQ
-A KUBE-SEP-JBFAMRDVQ5CON62O -p tcp -m tcp -j DNAT --to-destination 172.31.178.243:9300

通过路由规则找对应的pod(node到pod间通信)

# endpoint --> cluster ip or nodeip + nodeport --> client


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

***

### ipvs-ebpf

