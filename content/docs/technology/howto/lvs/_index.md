---
bookCollapseSection: false
weight: 1
title: "LVS"
---

# LVS

## 基础概念

### 术语

* *IPVS,ipvs,ip_vs*：内核模块，在director上提供负载均衡功能
* *LVS, linux virtual server* ：由 *director* + *realservers*组成*virtual server*，对client显示为一台机器
* *director*: 运行ipvs代码的节点，client连接director，director转发数据包到realserver，director只是具有使LVS正常工作的特殊规则的IP路由器
* *realservers*：运行服务的主机，处理来自client的请求
* *client* 
* *forwarding method* (currently [LVS-NAT](https://docs.huihoo.com/hpc-cluster/linux-virtual-server/HOWTO/LVS-HOWTO.LVS-NAT.html#LVS-HOWTO.LVS-NAT), [LVS-DR](https://docs.huihoo.com/hpc-cluster/linux-virtual-server/HOWTO/LVS-HOWTO.LVS-DR.html#LVS-HOWTO.LVS-DR), [LVS-Tun](https://docs.huihoo.com/hpc-cluster/linux-virtual-server/HOWTO/LVS-HOWTO.LVS-Tun.html#LVS-HOWTO.LVS-Tun))：决定director如何发送数据包给realserver 
* *scheduling* ([ipvsadm and schedulers](https://docs.huihoo.com/hpc-cluster/linux-virtual-server/HOWTO/LVS-HOWTO.ipvsadm.html#LVS-HOWTO.ipvsadm))：director用于选择realserver以便为来自client的新连接请求提供服务的算法

***

### LVS中IP/网络的名称

```
                        ________
                       |        |
                       | client | (local or on internet)
                       |________|
                          CIP
                           |
--                      (router)
                          DGW
                           | outside network
                           |
L                         VIP
i                      ____|_____
n                     |          | (director can have 1 or 2 NICs)
u                     | director |
x                     |__________|
                      DIP (and PIP)
V                          |
i                          | DRIP network
r         ----------------------------------
t         |                |               |
u         |                |               |
a        RIP1             RIP2            RIP3
l    _____________   _____________   _____________
    |             | |             | |             |
S   | realserver1 | | realserver2 | | realserver3 |
e   |_____________| |_____________| |_____________|
r
v
e
r
---
```

```
client IP     = CIP
virtual IP    = VIP - the IP on the director that the client connects to)
director IP   = DIP - the IP on the director in the DIP/RIP (DRIP) network
   (this is the realserver gateway for LVS-NAT)
realserver IP = RIP (and RIP1, RIP2...) the IP on the realserver
director GW   = DGW - the director's gw (only needed for LVS-NAT)
   (this can be the realserver gateway for LVS-DR and LVS-Tun)
```

***

## 负载均衡模式(转发方式)

### LVS-NAT

基于网络地址转换(NAT)实现，所有数据包都要经过director转发，realserver的gateway需配置为RIP

```
                        ________
                       |        |
                       | client | (local or on internet)
                       |________|
                           |
                        (router)
                       DIRECTOR_GW
                           |
--                         |
L                      Virtual IP
i                      ____|_____
n                     |          | (director can have 1 or 2 NICs)
u                     | director |
x                     |__________|
                          DIP
V                          |
i                          |
r         -----------------+----------------
t         |                |               |
u         |                |               |
a        RIP1             RIP2            RIP3
l   ____________     ____________     ____________
   |            |   |            |   |            |
S  | realserver |   | realserver |   | realserver |
e  |____________|   |____________|   |____________|
r
v
e
r
```



#### Flow Process

```markdown
1. client往VIP(director)发起请求 （source ip为cip，destination ip为vip）
2. director接收请求，ipvs模块在input链通过调度算法选择realserver，将数据包的目标IP和端口改为RIP的IP和端口(source ip为cip，destination ip为rip)
3. POSTROUTING链通过路由选路，将数据包发送给realserver
4. realserver处理请求，给director返回数据包(source ip为rip，destination ip为cip)
5. director接收数据包，修改数据包的源ip为vip，响应给client(source ip为vip，destination ip为cip)(iptables -t nat -A POSTROUTING -s RIP -j MASQUERADE)

```



***

### LVS-DR（direct routing）

通过更改数据包上的MAC地址并将数据包转发到realserver，realserver需在lo网卡上配置VIP

```
                        ________
                       |        |
                       | client | (local or on internet)
                       |________|
                           |
                        (router)-----------
                           |    SERVER_GW  |
--                         |               |
L                         VIP              |
i                      ____|_____          |
n                     |          | (director can have 1 or 2 NICs)
u                     | director |         |
x                     |__________|         |
                          DIP              |
V                          |               |
i                          |               |
r         -----------------+----------------
t         |                |               |
u         |                |               |
a      RIP1,VIP         RIP2,VIP        RIP3,VIP
l   ____________     ____________     ____________
   |            |   |            |   |            |
S  | realserver |   | realserver |   | realserver |
e  |____________|   |____________|   |____________|
r
v
e
r
```



#### Flow Process

```markdown
1. client请求vip(director) (cip-->vip)
2. director接收请求，ipvs模块在在input链通过调度算法选择realserver，将数据包的目标mac地址改为realserver的mac地址(cip-->vip)
3. realserver解析数据包，发现ip为自己的lo网卡上的ip，处理请求
4. realserver发送数据包经由gateway直接回复给client，(vip --> cip)
```



#### TCP状态机问题

```
#Director

1、SYN-RECEIVED (收到syn=1)
2、ESTABLISH(收到ack=1)
3、CLOSE_WAIT或者LAST_ACK(收到fin=1,ack=1)
4、超时机制
```



#### ARP问题

```markdown
# realserver
1. vip只能设置在lo网卡上，设置在其他网卡会响应arp request，造成arp table混乱
2. 抑制arp帧，
echo "1" >/proc/sys/net/ipv4/conf/all/arp_ignore
echo "2" >/proc/sys/net/ipv4/conf/all/arp_announce

arp_ignore参数（1）含义：只响应目标IP是本地真实网卡上配置的IP
arp_announce参数（2）含义：忽略报文的源IP地址，使用主机上能够跟用户通信的真实网卡发送数据

```



#### Keepalived集群问题

```
假设主备 director包含rs， 可以这样处理：

经过 director1 的包，如果 mac address 不是 director2 的，用 iptables 给包打 mark=i
经过 director2 的包，如果 mac address 不是 director1 的，用 iptables 给包打 mark=j
同时配置 LVS，不用三元组(ip,port,protocol)来表示 virtual_server，而用 fwmark-service，keepalived 配置 lvs 使用 fwmark-service。
这样，如果是 director 转发过来的包，就不会进入 LVS 进行负载（防止两个 director 互相扔皮球，进入死循环），而是被 RS 服务处理。而客户端进来的包，就会进入 LVS 进行负载。

iptables  -t mangle -I PREROUTING -d $VIP -p tcp -m tcp --dport $VPORT -m mac ! --mac-source $MAC_Director2 -j MARK --set-mark 0x3 
iptables  -t mangle -I PREROUTING -d $VIP -p tcp -m tcp --dport $VPORT -m mac ! --mac-source $MAC_Director1 -j MARK --set-mark 0x4


keealived
virtual_server fwmark 3  {  # node2 配置 fwmark 4
    delay_loop 10
    lb_algo rr
    lb_kind DR
    protocol TCP
  
    real_server RIP1 8080 {
    weight 1
    MISC_CHECK {
        # some check configuration
    }
    }
  
    real_server RIP2 8080 {
    weight 1
    MISC_CHECK {
        # some check configuration
        }
    }
```





***

### LVS-Tun（tunnelling）

数据包经过IP隧道技术封装并转发到realserver



***

## 调度算法

* round robin (rr), weighted round robin (wrr) ：轮询和按权重轮询
* least connected (lc), weighted least connection (wlc)：最小连接和按权重的最小连接

- [persistent connection](https://docs.huihoo.com/hpc-cluster/linux-virtual-server/HOWTO/LVS-HOWTO.persistent_connection.html#LVS-HOWTO.persistent_connection)
- LBLC: a persistent memory algorythm
- DH: destination hash
- SH: source hash

### 