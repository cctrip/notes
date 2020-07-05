# Firewalld

firewalld是CentOS7默认的防火墙服务，用于管理网络数据包的流动和转发。

***

### 基础命令

* 启动

		$ systemctl start firewalld.service

* 查看状态

		$ systemctl status firewalld.service

* 关闭

		$ systemctl stop firewalld.service

* 开启和关闭开机启动

		$ systemctl enable firewalld.service
		$ systemctl disable firewalld.service

* Rule配置：firewall-cmd命令

	Options              |   Description
  --------               | -------------
  -h, --help             |   Prints a short help text and exists
  -V, --version          |   Print the version string of firewalld
  -q, --quiet            |   Do not print status messages
  --state                |   Return and print firewalld state
  --reload               |   Reload firewall and keep state information
  --complete-reload      |   Reload firewall and loose state information
  --runtime-to-permanent |   Create permanent from runtime configuration
  --permanent            |   Set an option permanently
  --zone=&lt;zone>       |   Use this zone to set or query options, else default zone
  --timeout=&lt;timeval>    |   Enable an option for timeval time, where timeval is,a number followed by one of letters 's' or 'm' or 'h'


***

### 概念

#### 区域(Zones)

一个规则管理群组的概念，定义了可信任级别。其中预先定义的zones有以下几个：

* drop

	最低信任级别，任何流入网络的包都被丢弃，不作出任何响应。只允许流出的网络连接。

* block

	任何进入的网络连接都被拒绝，并返回 IPv4 的 icmp-host-prohibited 报文或者 IPv6 的 icmp6-adm-prohibited 报文。只允许由该系统初始化的网络连接。

* public

	用以可以公开的部分。你认为网络中其他的计算机不可信并且可能伤害你的计算机。只允许选中的连接接入。

* external

	用在路由器等启用伪装的外部网络。你认为网络中其他的计算机不可信并且可能伤害你的计算机。只允许选中的连接接入。

* internal

	用在内部网络。你信任网络中的大多数计算机不会影响你的计算机。只接受被选中的连接。

* dmz

	用以允许隔离区（dmz）中的电脑有限地被外界网络访问。只接受被选中的连接。

* work

	用在工作网络。你信任网络中的大多数计算机不会影响你的计算机。只接受被选中的连接。

* home

	用在家庭网络。你信任网络中的大多数计算机不会影响你的计算机。只接受被选中的连接。

* trusted

	允许所有网络连接。

#### 服务(service)

服务是端口和/或协议入口的组合。备选内容包括 netfilter 助手模块以及 IPv4、IPv6地址。


#### 端口和协议(port/protocol)

定义了 tcp 或 udp 端口，端口可以是一个端口或者端口范围。


#### ICMP阻塞

可以选择 Internet 控制报文协议的报文。这些报文可以是信息请求亦可是对信息请求或错误条件创建的响应.


#### 伪装

私有网络地址可以被映射到公开的IP地址。这是一次正规的地址转换。

### 端口转发

端口可以映射到另一个端口以及/或者其他主机。

***


### 配置文件

* 区域配置文件

		/usr/lib/firewalld/zones(原始文件目录)

	* 配置文件目录

			/etc/firewalld/zones

	* 配置文件格式

			<?xml version="1.0" encoding="utf-8"?>
			<zone>
  				<short>Public</short>     <!--区域名称-->
  				<description>For use in public areas. You do not trust the other computers on networks to not harm your computer. Only selected incoming connections are accepted.</description>
  				<service name="dhcpv6-client"/>
  				<service name="ssh"/>    <!--服务名称,调用ssh服务配置文件-->
  				<port protocol="tcp" port="2222"/>    <!--协议、端口-->
			</zone>

* 服务配置文件

		/usr/lib/firewalld/services (原始文件目录)

	* 配置文件目录

			/etc/firewalld/zones (zones优先调用目录)

	* 配置文件格式

			<?xml version="1.0" encoding="utf-8"?>
			<service>
  				<short>SSH</short>  <!--服务名称-->
  				<description>Secure Shell (SSH) is a protocol for logging into and executing commands on remote machines. It provides secure encrypted communications. If you plan on accessing your machine remotely via SSH over a firewalled interface, enable this option. You need the openssh-server package installed for this option to be useful.</description>
  				<port protocol="tcp" port="22"/>  <!--配置协议端口-->
			</service>


