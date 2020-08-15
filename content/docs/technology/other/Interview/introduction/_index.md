---
bookCollapseSection: false
weight: 1
title: "Prepare"
---

# Prepare

### 介绍

```
目前就职于cf的运维开发岗位，主要工作内容是开发运维自动化相关工具和平台，对公司技术部门提供系统、网络、nginx、云服务相关的技术支持。
入职以来主要做了以下几件事，1、制定运维基础元数据规范，2、开发资源自动化系统，对接不同的云平台，实现资源申请到发布一键化操作。3、搭建和二次开发监控系统，实现基础资源的统一监控、展示和告警。 4、利用ngx_lua实现限源功能，防攻击脚本，对接应用平台，实现项目环境的快速搭建。
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

1、interface接口规范，接入一个云平台只需要实现对应的方式就行

2、中间逻辑失败怎么处理
分两种情况，一种属于资源未创建成功，提供3次重试，都失败返回错误
一种是资源创建成功，推送各个平台失败
对于无特殊信息(密码之类的)，记录信息，提供推送接口，手动确认报错后，调用接口推送
有特殊信息，临时文件记录，提供推送接口，手动确认报错后，调用接口推送后，删除特殊信息

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
	传输优化
	压缩优化
	buffer优化
	timeout优化
	
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



# Nginx原理
# 健康检查(被动检查和主动)
# upstream
# 怎么查找host
# 怎么查找location
```

```
# Golang 并发
# Golang 内存模型
# Golang 垃圾回收
```

```
# k8s
# pod 与 pod 通信
# service通信
# storageclass
```

