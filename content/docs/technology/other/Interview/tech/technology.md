# 技术知识点

## 1. 计算机基础

***

## 硬件

### 1. 机器型号

```markdown
dmidecode | awk -F':' '/Product Name/{print $2}'
```

### 2. CPU信息

```
#获取逻辑CPU数
awk -F':' '/name/{print $2}' /proc/cpuinfo | wc -l
#获取CPU型号
awk -F':' '/name/{print $2}' /proc/cpuinfo | uniq
#获取物理cpu数
grep "physical id" /proc/cpuinfo | sort | uniq | wc -l
```

### 3. 内存信息

```
#获取内存大小
free -h
#内存物理信息
dmidecode -t memory
```

### 4. 磁盘信息

```

```

### 5. 计算机组成

```
1. 控制器
2. 运算器
3. 存储器
4. 输入设备
5. 输出设备
```



## 系统

***

## 网络

### 1. TCP协议

#### 1.1三次握手

    1、server端开启端口监听。(CLOSED-->LISTEN)
    2、client端发送SYN信息给server端。(CLOSED-->SYN-SENT)
    3、server端接收SYN信息，返回ACK信息和SYN信息给client端。(LISTEN-->SYN-RECEIVED)
    4、client端接收ACK和SYN信息，并返回一个ACK信息给server端.(SYN-SENT-->ESTABLISHED)
    5、server端接收ACK信息。(SYN-RECEIVED-->ESTABLISHED)
    6、连接建立

#### 1.2四次挥手

```markdown
1、client端主动发起关闭请求，发送FIN信息给server端(ESTABLISHED-->FIN-WAIT-1)
2、server端接收FIN信息，并返回一个ACK信息，等待应用确认关闭连接(ESTABLISHED-->CLOSE-WAIT)
3、client端接收ACK信息，等待server端的FIN信息(FIN-WAIT-1-->FIN-WAIT-2)
4、server端确认关闭，发送FIN信息给client端(CLOSE-WAIT-->LAST-ACK)
5、client端接收FIN信息，返回一个ACK信息。(FIN-WAIT-2-->TIME-WAIT)
6、server端接收ACK信息，关闭连接。(LASK-ACK-->CLOSED)
7、client端超时关闭连接。(TIME-WAIT-->CLOSED)
8、连接关闭
```

### 2. DNS

```markdown
1、查找本机缓存
2、查找本地hosts
3、查找路由器缓存
4、查找本地/ISP DNS服务器
5、查找根服务器
6、递归查询直到查到域名解析IP
7、本地DNS服务器缓存，返回给本机
```

### 3. HTTP

***

## WEB

### 1. CDN

```
1. client请求www.cctest.com
2. www.cctest.com CNAME 到 cctest.cdncache.com
3. CDN内部根据源IP得到离源IP最近的Cache服务器IP，并返回给client
4. client向Cache服务器发起请求
5. 请求内容存在，直接返回给client
6. 请求内容不存在，Cache服务器向RealServer请求内容
7. Cache服务器缓存RealServer的内容，并将内容返回给client
```

### 2.Lvs

四层负载均衡

```
1. client向LVS发起请求
2. LVS根据路由模式和调度算法分配realserver
3. client向realserver发起请求
```

路由模式:

* NAT

  ```
  1. client request load balance
  2. load balance 选择一台 realserver
  3. 更改packet的dest ip port 为realserver的ip port
  4. realserver接收并返回请求
  5. load balance 更改packet的source ip port 为 loadbalance的ip port
  ```

* DR

  ```
  1. client request load balance
  2. load balance 选择一台 realserver
  3. 更改目的mac地址，转发到realserver
  4. realserver接受请求，返回给client
  ```

* TUN

  ```
  1. client request load balance
  2. load balance 选择一台 realserver
  3. 通过tunnel将请求转发给realserver
  4. realserver接受请求，返回给client
  ```


调度算法：

```
1. rr
2. wrr
3. lc
4. wlc
5. lblc
6. lblcr
7. dh
8. sh
9. sed
10. nq
```



### 3.Nginx

WEB服务器，七层负载，反向代理

### 4.Tomcat

***

### 编程