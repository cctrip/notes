#!/bin/bash
#
#Written by: CC --2015/10/20
#


VERSION="apache-tomcat-7.0.64"
TIME=$(date +%Y%m%d%H%M)
WORKPATH=/opt/web/
PROJECT=$1

cd $WORKPATH
for pro in ${PROJECT}
do
	/etc/init.d/tomcat-service web-$pro stop
        echo "---Start update $pro tomcat-version to $VERSION---"
        tar -zxvf "$VERSION".tar.gz > /dev/null 2>&1
        mv $VERSION new-web-$pro
        rm new-web-$pro/webapps/* -rf > /dev/null 2>&1
        echo "---Start Copy---"
        cp web-$pro/bin/catalina.sh.new new-web-$pro/bin/catalina.sh
        cp web-$pro/conf/server.xml.new new-web-$pro/conf/server.xml
        cp web-$pro/conf/web.xml.new new-web-$pro/conf/web.xml
        cp -a web-$pro/webapps/$pro new-web-$pro/webapps/
        echo "---Start backups old $pro---"
        mv web-$pro bak/web-$pro.$TIME
        mv new-web-$pro web-$pro
        chown -R webrunner:webrunner web-$pro/*
        echo "---Update tomcat-version successful---"
        sh $WORKPATH/web-$pro/bin/version.sh
	/etc/init.d/tomcat-service web-$pro start
done
