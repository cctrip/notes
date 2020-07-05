#!/bin/bash


PACKAGEPATH="/usr/local/src"
VERSION="zabbix-3.0.1"
RETVAL=0

USERS=$(cat /etc/passwd | awk -F':' '{print $1}' | grep zabbix)
if [ -z "$USERS" ] ;then
        chattr -i /etc/passwd /etc/shadow /etc/group /etc/gshadow
    groupadd -g 201 zabbix
    useradd -g zabbix -u 201 -s /sbin/nologin zabbix
    chattr +i /etc/passwd /etc/shadow /etc/group /etc/gshadow
fi

cd $PACKAGEPATH
tar zxf $VERSION.tar.gz 2>&1 > /dev/null
cd $VERSION
./configure --prefix=/usr/local/zabbix --enable-agent
RETVAL=$?
if [ $RETVAL -eq 0 ];then
        make && make install
        RETVAL=$?
        if [ $RETVAL -eq 0 ];then
                echo "Install zabbix_agentd sucessful"
        else
                echo "something wrong,please check"
        exit 778
        fi
else
        echo "something wrong,please check"
        exit 777
fi

mkdir /var/log/zabbix
chown zabbix.zabbix /var/log/zabbix
cp misc/init.d/fedora/core/zabbix_agentd  /etc/init.d/
chmod 755 /etc/init.d/zabbix_agentd
sed -i "s@BASEDIR=/usr/local@BASEDIR=/usr/local/zabbix@g" /etc/init.d/zabbix_agentd
echo "please input zabbix server's IP"
read IP
sed -i "s@Server=127.0.0.1@Server=$IP@g" /usr/local/zabbix/etc/zabbix_agentd.conf
sed -i "s@ServerActive=127.0.0.1@ServerActive=$IP:10001@g" /usr/local/zabbix/etc/zabbix_agentd.conf
sed -i "s@tmp/zabbix_agentd.log@var/log/zabbix/zabbix_agentd.log@g"  /usr/local/zabbix/etc/zabbix_agentd.conf
sed -i "s@^# UnsafeUserParameters=0@UnsafeUserParameters=1\n@g" /usr/local/zabbix/etc/zabbix_agentd.conf
sed -i "Hostname=Zabbix server@Hostname=Test server@g" /usr/local/zabbix/etc/zabbix_agentd.conf

#启动zabbix_agentd
chkconfig zabbix_agentd on
service zabbix_agentd start
