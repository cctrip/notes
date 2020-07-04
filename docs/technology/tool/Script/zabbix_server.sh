#!/bin/bash
#
#Written by CC  --2015/11/27


PHPPATH="/usr/local/php"
MYSQLPATH="/usr/local/mysql"
PACKAGEPATH="/usr/local/src"
VERSION="zabbix-3.0.1"
RETVAL=0

function yumInstall() {
	yum -y install net-snmp net-snmp-devel	
}

function phpSet() {
	if [ -f $PHPPATH/etc/php.ini ];then
		sed -i "s@;date.timezone =@date.timezone = Asia/Shanghai@g" $PHPPATH/etc/php.ini
		sed -i "s@max_execution_time = 30@max_execution_time = 300@g" $PHPPATH/etc/php.ini
		sed -i "s@post_max_size = 8M@post_max_size = 32M@g" $PHPPATH/etc/php.ini
		sed -i "s@max_input_time = 60@max_input_time = 300@g" $PHPPATH/etc/php.ini
		sed -i "s@memory_limit = 128M@memory_limit = 128M@g" $PHPPATH/etc/php.ini
		sed -i "s@;mbstring.func_overload = 0@ambstring.func_overload = 2@g" $PHPPATH/etc/php.ini
		sed -i "s@;always_populate_raw_post_data = -1@always_populate_raw_post_data = -1@g" $PHPPATH/etc/php.ini
	else
		echo "something wrong ,please check $PHPPATH/etc/php.ini"
	fi
}

function zabbixInstall() {
	USERS=$(cat /etc/passwd | awk -F':' '{print $1}' | grep zabbix)
    if [ -z "$USERS" ] ;then
        chattr -i /etc/passwd /etc/shadow /etc/group /etc/gshadow
		groupadd -g 201 zabbix
		useradd -g zabbix -u 201 -s /sbin/nologin zabbix
        chattr +i /etc/passwd /etc/shadow /etc/group /etc/gshadow
	fi
	
	cd $PACKAGEPATH
	tar zxf $VERSION.tar.gz
	cd $VERSION
	./configure --prefix=/usr/local/zabbix --enable-server --enable-proxy --enable-agent --with-mysql=$MYSQLPATH/bin/mysql_config --with-net-snmp --with-libcurl
	RETVAL=$?
	if [ $RETVAL -eq 0 ];then
		make && make install
		RETVAL=$?
		if [ $RETVAL -eq 0 ];then
			echo "---Install zabbix sucessful!"
		else
			echo "something wrong,please check!"
			exit 777
		fi
	else
		echo "something wrong,please check!"
		exit 776
	fi

}


function dataAdd() {
	cd $PACKAGEPATH/$VERSION
	mysql -e "create database zabbix default charset utf8;"
	mysql -e "grant all on zabbix.* to zabbix@localhost identified by 'zabbix';"      
	mysql -uzabbix -pzabbix zabbix<./database/mysql/schema.sql
	mysql -uzabbix -pzabbix zabbix<./database/mysql/images.sql
	mysql -uzabbix -pzabbix zabbix<./database/mysql/data.sql
}

function otherSet() {
	mkdir /var/log/zabbix
	chown zabbix.zabbix /var/log/zabbix
	cp $PACKAGEPATH/$VERSION/misc/init.d/fedora/core/zabbix_* /etc/init.d
	chmod 755 /etc/init.d/zabbix_*

	#修改/etc/init.d目录下的zabbix_server和zabbix_agentd启动文件
	sed -i "s@BASEDIR=/usr/local@BASEDIR=/usr/local/zabbix@g" /etc/init.d/zabbix_server
	sed -i "s@BASEDIR=/usr/local@BASEDIR=/usr/local/zabbix@g" /etc/init.d/zabbix_agentd

	#修改/etc/zabbix/zabbix_server.conf
	sed -i "s@DBUser=root@DBUser=zabbix@g" /usr/local/zabbix/etc/zabbix_server.conf
	sed -i "s@#DBPassword=@DBPassword=zabbix@g" /usr/local/zabbix/etc/zabbix_server.conf
	sed -i "s@# DBPassword=@DBPassword=zabbix@g" /usr/local/zabbix/etc/zabbix_server.conf

	#修改/etc/zabbix/zabbix_agentd.conf，这里的IP地址写的是zabbix_server的IP地址，即172.16.0.104
	echo "please input zabbix server's IP"
	read IP
	sed -i "s@Server=127.0.0.1@Server=127.0.0.1,$IP@g" /etc/zabbix/zabbix_agentd.conf
	sed -i "s@ServerActive=127.0.0.1@ServerActive=$IP:10051@g" /etc/zabbix/zabbix_agentd.conf
	sed -i "s@tmp/zabbix_agentd.log@var/log/zabbix/zabbix_agentd.log@g" /etc/zabbix/zabbix_agentd.conf
	sed -i "s@^# UnsafeUserParameters=0@UnsafeUserParameters=1\n@g" /etc/zabbix/zabbix_agentd.conf

	#复制zabbix站点的文件到/var/www/html目录下
	cp -r $PACKAGEPATH/$VERSION/frontends/php/ /var/www/html/zabbix/
	chown -R www.www /var/www/html/zabbix/

	#启动服务
	chkconfig zabbix_server on
	chkconfig zabbix_agentd on
	service zabbix_server start
	service zabbix_agentd start
}

yumInstall
phpSet
zabbixInstall
dataAdd
otherSet
