#!/bin/bash
#
#Written by: CC  --2015/10/21
#

if [ -r /lib/lsb/init-functions ];then
        . /lib/lsb/init-functions
else
        exit 1
fi

WEBPATH=/cache1/web
TEMP=/cache1/web/tmp
RETVAL=0
PROJECT=$1

cd $TEMP
for pro in ${PROJECT}
do
	/etc/init.d/tomcat-service $pro stop
	if [ -d $pro ];then
		rm $WEBPATH/web-$pro/webapps/$pro -rf
		mv $pro $WEBPATH/web-$pro/webapps
		RETVAL=$?
		if [ $RETVAL -eq 0 ];then
			log_success_msg "Service $pro restore finish"	
			/etc/init.d/tomcat-service $pro start
		else
			log_failure_meg "Some wrong please check"
		fi
	else
		"$pro is not exists"
	fi
done
		
