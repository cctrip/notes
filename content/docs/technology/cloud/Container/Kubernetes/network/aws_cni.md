---
bookCollapseSection: false
weight: 4
title: "AWS VPC CNI"
---

# AWS VPC CNI

## Goal

### K8S网络需求

* Pod之间的通信不需要通过NAT转换
* Node和Pod通信不需要通过NAT转换
* Pod所看到的IP地址与其他人所看到的IP地址相同

***

### K8S运行在AWS VPC上的目标

* Pod联网必须支持与用户从EC2联网中获得的特性相当的高吞吐量和可用性，低延迟和最小抖动
* 可以使用跟EC2一样的网络安全组
* 网络操作必须简单安全。用户必须能够应用现有的AWS VPC网络和安全最佳实践，以通过AWS VPC构建Kubernetes集群
* 只需几秒钟即可设置Pod网络
* 管理员应能够将群集扩展到2000个节点

***

## 方案

* 为每个Node(ec2)创建多个弹性网络接口(ENIs)，并分配secondary IP
* 对于每个Pod，选择一个可用的secondary IP，将其分配给Pod，并实现以下功能：
  * 在单个主机上进行Pod到Pod的通信
  * 在不同主机上进行Pod到Pod的通信
  * 允许在Pod和AWS服务进行通信
  * 允许Pod和本地数据中心进行通信
  * 允许Pod和Internet进行通信



> 在EC2-VPC里，每个实例可以创建多个ENI，每个ENI可以分配多个IP地址。 任何发往这些IP地址之一的数据包，EC2-VPC都会将该数据包传递到实例。
>
> ENI是虚拟网络接口，您可以将其附加到VPC中的实例。 将ENI附加到实例后，将创建一个对应的接口。 主ENI IP地址会自动分配给该接口。 所有辅助地址均未分配，并且由主机所有者决定如何配置它们。

***

## 架构

### Pod To Pod

![img](https://github.com/aws/amazon-vpc-cni-k8s/raw/master/docs/images/wire-network.png)

***

#### Inside a Pod

IP address

```shell
# ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
3: eth0@if173: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9001 qdisc noqueue state UP group default
    link/ether 6a:f3:a1:ff:38:a8 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 172.31.176.184/32 scope global eth0
       valid_lft forever preferred_lft forever
```

route

```shell
# ip route show
default via 169.254.1.1 dev eth0
169.254.1.1 dev eth0 scope link
```

static arp

```shell
# arp -a
172-31-177-243.node-exporter.monitoring.svc.cluster.local (172.31.177.243) at 8e:6b:e1:80:7c:de [ether] on eth0
_gateway (169.254.1.1) at 8e:6b:e1:80:7c:de [ether] PERM on eth0
```

#### On Host side

ip address

```shell
# ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9001 qdisc mq state UP group default qlen 1000
    link/ether 02:b1:bf:9a:b2:cb brd ff:ff:ff:ff:ff:ff
    inet 172.31.177.243/23 brd 172.31.177.255 scope global dynamic eth0
       valid_lft 2539sec preferred_lft 2539sec
    inet6 fe80::b1:bfff:fe9a:b2cb/64 scope link
       valid_lft forever preferred_lft forever
8: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9001 qdisc mq state UP group default qlen 1000
    link/ether 02:cd:2d:55:75:29 brd ff:ff:ff:ff:ff:ff
    inet 172.31.177.128/23 brd 172.31.177.255 scope global eth1
       valid_lft forever preferred_lft forever
    inet6 fe80::cd:2dff:fe55:7529/64 scope link
       valid_lft forever preferred_lft forever
173: enic614534eb15@if3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9001 qdisc noqueue state UP group default
    link/ether 8e:6b:e1:80:7c:de brd ff:ff:ff:ff:ff:ff link-netnsid 3
    inet6 fe80::8c6b:e1ff:fe80:7cde/64 scope link
       valid_lft forever preferred_lft forever
```

通过路由表控制Pod的出入流量

* main route控制进入pod的流量

  ```shell
  # ip route show
  default via 172.31.176.1 dev eth0
  169.254.169.254 dev eth0
  172.31.176.0/23 dev eth0 proto kernel scope link src 172.31.177.243
  172.31.176.184 dev enic614534eb15 scope link   # <----- Pod's IP 
  ```

* 每个ENI都有自己的路由表，该路由表用于路由Pod的传出流量。

  ```shell
  # ip route show table 2
  default via 172.31.176.1 dev eth1
  172.31.176.1 dev eth1 scope link
  ```

* 需要给pod ip配置策略路由，否则流量无法走到ENI的路由表

  ```shell
  # ip rule list
  0:	from all lookup local
  512:	from all to 172.31.176.184 lookup main  --> 到Pod的流量走默认路由表
  1024:	from all fwmark 0x80/0x80 lookup main
  1536:	from 172.31.176.184 lookup 2            --> 从Pod出来的流量走ENI自己的路由表     
  32766:	from all lookup main
  32767:	from all lookup default
  ```

#### CNI插件执行的操作

* 创建veth pair，一个放到主机的namespace，一个放到Pod's namespace

  ```markdown
  ip link add veth-1 type veth peer name veth-1c  /* on host namespace */
  ip link set veth-1c netns ns1  /* move veth-1c to Pod's namespace ns1 */
  ip link set veth-1 up /* bring up veth-1 */
  ip netns exec ns1 ip link set veth-1c up /* bring up veth-1c */
  ```

* 获取分配给实例的secondary IP地址，并在Pod的namespace中执行以下操作：

  * 分配IP给Pod的eth0
  * 添加默认网关和默认路由到Pod的路由表
  * 给默认网关添加静态ARP条目

  ```markdown
  /* To assign IP address 172.31.176.184 to Pod's namespace ns1 */
   ip netns exec ns1 ip addr add 172.31.176.184/32 dev veth-1c /* assign a IP address to veth-1c */
   ip netns exec ns1 ip route add 169.254.1.1 dev veth-1c /* add default gateway */ 
   ip netns exec ns1 ip route add default via 169.254.1.1 dev veth-1c /* add default route */
  
   ip netns exec ns1 arp -i veth-1c -s 169.254.1.1 <veth-1's mac> /* add static ARP entry for default gateway */
  ```

* 在主机上添加到Pod的路由

  ```markdown
  /* Pod's IP address is 172.31.176.184 */
   ip route add 172.31.176.184/32 dev veth-1 /* add host route */
  ```



#### 流量过程

```markdown
#以172.31.176.184为例说明node1's pod1 to node2's pod2的流量发出过程
1. pod1的默认出口为169.254.1.1(mac地址为veth pair的另一端)
2. 匹配策略路由from 172.31.176.184 lookup 2
3. 匹配路由表2 default via 172.31.176.1 dev eth1，流量从node1的eth1出口出去
4. EC2-VPC流量转发到node2的ethX

#通过172.31.176.184为例解释node2's pod2的接收过程
5. 流量进入node2的eth1接口
6. 匹配策略路由from all to 172.31.176.184 lookup main
7. 匹配路由表main 172.31.176.184 dev enic614534eb15 scope link,流量发往enic614534eb15接口
8. 通过veth pair传输给pod2

```



![img](https://github.com/aws/amazon-vpc-cni-k8s/raw/master/docs/images/ping.png)

***

### Pod To External

![img](https://github.com/aws/amazon-vpc-cni-k8s/raw/master/docs/images/ping2external.png)

#### AWS_VPC_K8S_CNI_EXTERNALSNAT = False

使用iptables SNAT规则，将pod ip转换成主ENI的主IP地址

```
-A POSTROUTING ! -d <VPC-CIDR> -m comment --comment "kubenetes: SNAT for outbound traffic from cluster" -m addrtype ! --dst-typ
```



#### AWS_VPC_K8S_CNI_EXTERNALSNAT = True

当将SNAT功能关闭后，无法通过主ENI的主IP地址做外网映射，此时需要给对应的ENI的主IP地址配置对应的外网IP，或者给子网配置默认网关

***



https://github.com/aws/amazon-vpc-cni-k8s/blob/master/docs/cni-proposal.md