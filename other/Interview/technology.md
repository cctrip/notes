# 技术知识点

## 系统

***

## 网络

###1. TCP协议

#### 1.1三次握手
    
    1. server端开启端口监听。(CLOSED-->LISTEN)
    2. client端发送SYN信息给server端。(CLOSED-->SYN-SENT)
    3. server端接收SYN信息，返回ACK信息和SYN信息给client端。(LISTEN-->SYN-RECEIVED)
    4. client端接收ACK和SYN信息，并返回一个ACK信息给server端.(SYN-SENT-->ESTABLISHED)
    5. server端接收ACK信息。(SYN-RECEIVED-->ESTABLISHED)
    5. 连接建立

#### 1.2四次挥手

    1. client端主动发起关闭请求，发送FIN信息给server端(ESTABLISHED-->FIN-WAIT-1)
    2. server端接收FIN信息，并返回一个ACK信息，等待应用确认关闭连接(ESTABLISHED-->CLOSE-WAIT)
    3. client端接收ACK信息，等待server端的FIN信息(FIN-WAIT-1-->FIN-WAIT-2)
    4. server端确认关闭，发送FIN信息给client端(CLOSE-WAIT-->LAST-ACK)
    5. client端接收FIN信息，返回一个ACK信息。(FIN-WAIT-2-->TIME-WAIT)
    6. server端接收ACK信息，关闭连接。(LASK-ACK-->CLOSED)
    7. client端超时关闭连接。(TIME-WAIT-->CLOSED)
    7. 连接关闭

###2. DNS

    1. 查找本机缓存
    2. 查找本地hosts
    3. 查找路由器缓存
    4. 查找本地/ISP DNS服务器
    5. 查找根服务器
    6. 递归查询直到查到域名解析IP
    7. 本地DNS服务器缓存，返回给本机

###3. HTTP

***

### WEB

***

### 大数据

***

### 编程