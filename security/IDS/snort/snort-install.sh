#!/bin/bash
#
#Description: snort simple install
#
#Written by: CC --2015/12/11

SVERSION="snort-2.9.8.0"
DVERSION="daq-2.0.6"
PACKAGEDIR="/usr/local/src/snort"
RETVAL=0


function yumInstall() {
	echo "---Starting yum install---"
	yum -y install gcc flex bison zlib zlib-devel pcre pcre-devel tcpdump libdnet.x86_64 libdnet-devel.x86_64
	yum -y install libmnl.x86_64 libmnl-devel.x86_64 libnfnetlink.x86_64 libnfnetlink-devel.x86_64 libnetfilter_queue.x86_64 libnetfilter_queue-devel.x86_64
}

function libPathAdd() {
	if [ -f /etc/ld.so.conf.d/local.conf ];then
		cat /etc/ld.so.conf.d/local.conf | grep "/usr/local/lib64"
		RETVAL=$?
		if [ $RETVAL -ne 0 ];then
			echo "/usr/local/lib64" >> /etc/ld.so.conf.d/local.conf
		fi
	else
		touch /etc/ld.so.conf.d/local.conf
		echo "/usr/local/lib64" >> /etc/ld.so.conf.d/local.conf
	fi
}

function pcapInstall() {
	cd $PACKAGEDIR
	tar -zxf libpcap-1.7.4.tar.gz
	cd libpcap-1.7.4
	./configure --prefix=/usr/local --libdir=/usr/local/lib64 2>&1 >> snortinstall.log
	RETVAL=$?
	if [ $RETVAL -eq 0 ];then
		make && make install 
		RETVAL=$?
		if [ $RETVAL -eq 0 ];then
			echo "sucessful"
		else 
			echo "something wrong,please check!"
			exit 1
		fi
	else
		echo "something wrong,please check snortinstall.log!"
		exit 1
	fi
}


function daqInstall() {
	cd $PACKAGEDIR
	tar -zxf $DVERSION.tar.gz
	cd $DVERSION
	./configure --prefix=/usr/local --libdir=/usr/local/lib64 2>&1 >> snortinstall.log
	RETVAL=$?
    if [ $RETVAL -eq 0 ];then
        make && make install
        RETVAL=$?
        if [ $RETVAL -eq 0 ];then
            echo "sucessful"
        else
            echo "something wrong,please check!"
            exit 1
        fi
    else
        echo "something wrong,please check snortinstall.log!"
        exit 1
    fi	
}

function snortInstall() {
	cd $PACKAGEDIR
    tar -zxf $SVERSION.tar.gz
    cd $SVERSION
    ./configure --prefix=/usr/local/snort 2>&1 >> snortinstall.log
    RETVAL=$?
    if [ $RETVAL -eq 0 ];then
        make && make install
        RETVAL=$?
        if [ $RETVAL -eq 0 ];then
            echo "sucessful"
        else
            echo "something wrong,please check!"
            exit 1
        fi
    else
        echo "something wrong,please check snortinstall.log!"
        exit 1
    fi
}

function snortConf() {
	cd $PACKAGEDIR 
	cp snortd /etc/init.d/
	chmod a+x /etc/init.d/snortd
	cp snort /etc/sysconfig/
	tar -zxf snortrule.tar.gz -C /etc/
}


yumInstall
libPathAdd
pcapInstall
snortInstall
snortConf
