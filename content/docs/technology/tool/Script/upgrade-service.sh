#!/bin/bash
#
#Written by: CC   --2015/10/20
#

if [ -r /lib/lsb/init-functions ];then
	. /lib/lsb/init-functions
else
	exit 1
fi

WEBPATH=/cache1/web
BACKPATH=/cache1/web/appbak
WARPATH=/cache1/web/sadir
TEMP=/cache1/web/tmp
TIME=`date +%Y%m%d%H%M`

PROJECT=$1
RETVAL=0

cd $WARPATH
for pro in ${PROJECT[@]}
do
	#uncompress app
	mkdir $pro
	unzip $pro.war -d $pro > /dev/null 2>&1
	RETVAL=$?
	if [ $RETVAL -eq 0 ];then
		cp -a $WARPATH/conf/$pro/* $WARPATH/$pro/WEB-INF/classes/  >/dev/null 2>&1
		chown -R webrunner:webrunner $pro
		#backups old app and deploy new app
		rm $TEMP/$pro -rf >/dev/null 2>&1
		/etc/init.d/tomcat-service web-$pro stop
		cp -a $WEBPATH/web-$pro/webapps/$pro $TEMP >/dev/null 2>&1
		mv $WEBPATH/web-$pro/webapps/$pro $BACKPATH/$pro-$TIME
		mv $WARPATH/$pro $WEBPATH/web-$pro/webapps/
		RETVAL=$?

		if [ $RETVAL -eq 0 ];then
			log_success_msg "Deploy $pro finish"
			/etc/init.d/tomcat-service web-$pro start
		else
			echo "something wrong please check"
		fi
	else
		echo "uncompress $pro fail"
	fi	
			
done		
