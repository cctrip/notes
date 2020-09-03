---
bookCollapseSection: false
weight: 1
title: "Prepare"
bookToc: false
---

# Prepare

### 介绍

```
目前就职于cf的运维开发岗位，主要工作内容是开发运维自动化相关工具和平台，对公司技术部门提供系统、网络、nginx、云服务相关的技术支持。
入职以来主要做了以下几件事，1、制定运维基础元数据规范，2、开发资源自动化系统，对接不同的云平台，实现资源申请到发布一键化操作。3、搭建和二次开发监控系统，实现基础资源的统一监控、展示和告警。 4、利用ngx_lua实现限源功能，防攻击脚本，对接应用平台，实现项目环境的快速搭建。5、搭建k8s平台，落地k8s监控和日志系统。
```

***

### 可能碰到的问题

#### 项目

```markdown
# cmdb怎么做
以应用为维度，分为三部分，第一部分是应用自己的信息，包括代码地址，代码类型、应用端口等信息，第二部分是应用归属，包括owner和部门，第三部分为资源信息，包括资源类型、环境、以及连接信息
```

| 应用 | 语言 | git地址 |
| ---- | ---- | ------- |
|      |      |         |

| 应用 | owner | 部门 |
| ---- | ----- | ---- |
|      |       |      |

| 应用 | 环境 | 资源类型 | 资源 |
| ---- | ---- | -------- | ---- |
|      |      |          |      |

| 资源 | 资源类型 | 资源信息 |
| ---- | -------- | -------- |
|      |          |          |

```
# 项目亮点和难点

目前接入哪些服务,ecs,rds,redis,slb,

1、interface接口规范，接入一个云平台只需要实现对应的方式就行

2、中间逻辑失败怎么处理
分两种情况，一种属于资源未创建成功，提供3次重试，都失败返回错误
一种是资源创建成功，推送各个平台失败
对于无特殊信息(密码之类的)，记录信息，提供推送接口，手动确认报错后，重试，完成后删除信息
有特殊信息，临时文件记录，提供推送接口，手动确认报错后，调用接口推送后，删除特殊信息，密码做记录

```



```
# 监控系统
# 数据采集 ecs、rds、redis、lb、cdn
# 阈值平台，rule-engine单独出来，定时到gateway拉取告警配置，然后拉取Prometheus接口做计算，告警推送到gateway，对用户不支持自定义指标
# 告警收敛
```



```
# ngx_lua
# 限源怎么做，利用ngx_shared dict，最小计算单元，10秒，至少两个周期，ip_time(最小计算单元)，  ip_time + n个周期的总数，超过就deny，进来的流量先判断是否deny，deny配置过期时间

# 路由怎么做，配置泛域名，解析域名跟url，请求应用平台，取得proxy_pass返回值

```



```
# 系统优化
	tcp优化
	
# nginx优化
	传输优化, sendfile, tcp_nopush, tcp_nodelay
	压缩优化, gzip, level 2, text type
	buffer优化,   buffer_size, header_buffer_size, proxy,  temp_file
	timeout优化,  keepalive_timeout, send_timeout,read_timeout
	
```





### 技术问题

```
# TCP三次握手和四次挥手
### 三次握手
1、server端创建socket，监听某个端口，server端进入listen状态
2、client端创建socket，根据local_port_range随机选择一个未使用的端口，并生成ISN随机序列号，SYN标志位1，往server发送syn包，进入syn-sent状态
3、server端接收到数据包，若该数据包未超过sync_backlog半连接的队列大小，处理数据表，生成自己的ISN，将ack number配置为对方ISN+1，将syn和ack标志位1，发送给client，进入syn-received状态
4、client接收到syn包，回复一个ack number为ISN+1，ack标志位为1的数据包，进入Establish状态
5、server接收到ack包，进入accept队列(somaxconn)，复制一个socket来处理该连接，进入establish状态

### 四次挥手
1、client发送一个FIN和ACK标志都为1的数据包，进入FIN_WAIT_1状态
2、server接收到该数据包，立即返回一个ACK包，进入CLOSE_WAIT状态，等待程序处理完，关闭连接
3、client接收到ACK包后，进入FIN_WAIT_2的状态，等待对方的FIN数据包
4、server处理完后，发送FIN包给client，进入LAST_ACK状态，等待对方的ACK包
5、client接收到FIN后，发送ACK，进入TIME_WAIT状态，等待超时进入CLOSED
6、server接收到ACK包，关闭socket
7、特殊情况，client和server同时发送FIN，即两个都进入CLOSING状态。即发送FIN后，未收到ACK，确收到对方的FIN包的时候。 

# HTTP结构
请求行，method，url，version
请求头，host, content-type,length, cache-control, cors配置，cookie, authrozation
请求体，

响应行，
响应头，
响应体

# HTTP缺点
# HTTP2优势

# DNS解析过程
1、查找本地缓存，/etc/hosts
2、查找本地DNS服务器，/etc/resolv.conf(递归)
3、查找根服务，.，
4、查找一级域名DNS服务器，.com.
5、查找二级域名DNS服务器，.xxx.com.
...

```

```
# 负载均衡
# LVS+Keepalived原理
# LVS NAT
1、prerouting接收数据包，进入input前，ipvs更改目标地址和端口，forward进入postrouting出去
2、realserver配置的网关为director的ip，将数据包发送给director，director SNAT发送给client

# LVS DR
1、prerouting接收数据包，进入input前，ipvs更改目标mac地址，讲数据包转发给realserver
2、realserver将数据包直接返回给client，(arp抑制)，主要是不发送自己的arp信息，以及发包的时候，忽略源ip信息，直接通过发出去的接口的mac地址
3、director状态机，通过标志位判断，syn，进入syn-received,ack，establish，  fin+ack， 接入LAST-ACK状态

# keepalived
如何做健康检查，arrp通信
当director和realserver同一台时，需mark mac地址


# Nginx原理
master和worker几点，worker处理真实请求
epoll，异步非阻塞

# 健康检查(被动检查和主动)
被动，3次失败，10秒不可用

# upstream
轮询，权重轮询，最小连接， ip_hash
# 怎么查找host
ip:port+ server_name是唯一标识
server_name 存储结构
完全匹配，前通配符匹配，后通配符匹配
regex 正则匹配的server
default_server


# 怎么查找location
1、完全匹配
2、前缀匹配选最长，判断最长匹配前缀是否带^~非正则匹配
3、正则匹配
4、最长前缀匹配
```

```
# Golang 并发
进程：分配资源的基本单位，独立的栈空间，独立的堆空间，进程之间调度由os完成
线程：独立运行和独立调度的基本单位，独立的栈空间，共享堆空间，内核线程之间调度由os完成
协程：用户级线程，独立的栈空间，共享堆空间，调度由用户自己控制，协作式调度，主动转让控制权
goroutine：Golang自己实现的协程，不完全协作式调度，由go自己实现的调度器调度。

内存消耗方面
每个 goroutine (协程) 默认占用内存远比 Java 、C 的线程少。
goroutine：2KB
线程：1MB

线程和 goroutine 切换调度开销方面
线程/goroutine 切换开销方面，goroutine 远比线程小
线程：涉及模式切换(从用户态切换到内核态)、16个寄存器、PC、SP...等寄存器的刷新等。
goroutine：只有三个寄存器的值修改 - PC / SP / DX.

channel
不通过共享内存来通信，而是通过通信来共享内存


# Golang 垃圾回收
三色标记法+混合写屏障

根对象
全局变量：程序在编译期就能确定的那些存在于程序整个生命周期的变量。
执行栈：每个 goroutine 都包含自己的执行栈，这些执行栈上包含栈上的变量及指向分配的堆内存区块的指针。
寄存器：寄存器的值可能表示一个指针，参与计算的这些指针可能指向某些赋值器分配的堆内存区块。

1、标记准备，开启写屏障
2、查找根对象，标记为灰色
3、查找灰色对象，将灰色对象标记为黑色，将黑色对象的子节点标记为灰色
4、重复3，直到只剩黑色对象和白色对象
5、标记过程中更改，删除指针时，将自己标记为灰色，新增指针时，将对方标记为灰色

```

```
# k8s
# pod 与 pod 通信
云平台插件，
1、新增eni(弹性网卡)，每张网卡可以绑定n个辅助ip，给pod使用，增加一张eni的路由表，到网关的走这张网卡出去
2、创建pod，新增veth pair，一端挂载到pod的namesapce，一端挂载到node的namespace
3、新增2条策略路由，所有到pod ip的数据都走默认路由表，所有从pod ip出来的数据都走eni网卡的路由表
4、新增一条路由，所有到pod ip的数据都走veth网卡
5、之后就是VPC处理出来的数据了

flannl
1、新增一条到xxxx/24的路由到flnanel.0的网卡
2、flannel处理，pod增加自己的mac头部和下一跳(flannel.0)的mac地址到数据包，增加vxlan头部，增加udp头部，查找bgf，增加ip头部，正常的网络流量处理
3、解包到pod ip，处理数据

# service通信
iptables
prerouting，output链， kube-service链，kube-svc（kube-node）,kube-sep,dnat操作,nf_track

ipvs
prerouting，ipvs dnat，postrouting，


# storageclass
```



### 其他

```
#为什么选sdet
1. 测试和运维技术相通，环境不同，但是目的是一致。
2. devops最终的结局可能会只剩下业务开发和平台开发，做开发是技术职业方向
3. 这几年做的都是内部平台内的工作，基本是维护所有环境

```

