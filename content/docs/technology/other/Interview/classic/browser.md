# 经典问题

### 1. 当输入google.com时，发生了什么？

#### 1.1 URL解析

当输入的URL不合法时，浏览器会将输入的字符传给默认搜索引擎，

浏览器通过URL能知道以下信息：

```markdown
protocol: http
host: google.com
resource: /
```



#### 1.2 HTST

```markdown
1、浏览器检查自身的HTST列表，确认是否包含该主机。
2、若HTST存在该主机，使用https代替http，否则使用http。
```



#### 1.3 DNS解析

```markdown
1、浏览器检查自身的DNS缓存
2、查找本地hosts文件
3、发起DNS解析查询
4、查询 本地|ISP DNS服务器 
5、本地|ISP DNS服务器像高层服务器发起递归查询直到查到该域名的解析IP
```



#### 1.4 TCP连接建立

```markdown
1、client端发送SYN请求到server端，声明自己的ISN为aaa (CLOSED-->SYN-SENT)
2、server端接收SYN包，声明自己的ISN为bbb，ACK信息为aaa+1，返回给client端 (LISTEN-->SYN-RECEIVED)
3、client端返回ACK为bbb+1为server端 (SYN-SENT-->ESTABLISHED)
4、数据交互
```



#### 1.5 TLS连接建立

#### 1.6 HTTP

***







