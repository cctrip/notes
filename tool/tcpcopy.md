# TCPCopy

TCPCopy是一个流量复制工具。

***

### 使用场景

* 压力测试

* 模拟实际场景

* 回归测试

* 性能对照

***

### 架构

![架构](tcpcopy-arch.gif)

***
TCPCopy包含两部分：

* tcpcopy

	安装在线上服务器上，用于抓取线上的请求包

* intercept

	安装在辅助服务器上，做一些辅助作业


***

### 安装使用

设备：

online server：线上机器(流量导出的机器)

target server：测试机器(流量导入的机器)

assistant server：辅助机器

1. 在target server上添加路由

		$ route add -net CLINET_NET gw ASSISTANG_IP

2. 在assistant server上安装intercept服务

	下载地址：[https://github.com/session-replay-tools/intercept/releases](https://github.com/session-replay-tools/intercept/releases)

	安装：

		$ cd intercept
		$ ./configure --prefix=/usr/local/intercept
		$ make && make insall
		
	启动：

		$ /usr/local/intercept/sbin/intercept -i eth0 -F tcp and src host TARGET_IP and src port 8087 -d

3. 在online server安装tcpcopy服务

	下载地址：[https://github.com/session-replay-tools/tcpcopy/releases](https://github.com/session-replay-tools/tcpcopy/releases)

	安装：

		$ cd tcpcopy
		$ ./configure --prefix=/usr/local/intercept
		$ make && make install

	启动

		$ /usr/local/tcpcopy/sbin/tcpcopy -x ONLINE_IP:PORT-TARGET_IP:PORT -s ASSISTAND_IP -c CLIENT_IP -d

***
