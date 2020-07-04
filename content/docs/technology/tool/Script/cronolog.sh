#!/bin/bash
#
#Written by: CC  --2015/10/20
#

NAME=cronolog-1.6.2
INSPATH=/cache1/soft/${NAME}.tar.gz
WEBDIR=/cache1/web/web-$1


function install() {
which cronolog > /dev/null
if [ $? -ne 0 ];then
        if [ -f $INSPATH ];then
                tar -zxvf $INSPATH 2>&1 > /dev/null
                if [ -d $NAME ];then
                        cd $NAME
                        ./configure && make && make install
                        cd ..
                        rm $NAME -rf
                        echo "------------install finish------------"
                else
                        echo "The $NAME is not exist"
                fi
        else
                echo "The $INSPATH is not exist "
        fi
fi
}

function alterConf() {
        if [ -d $WEBDIR ];then
                cd $WEBDIR/bin/
                cp catalina.sh catalina.sh.bak
                sed -i 's#CATALINA_OUT="$CATALINA_BASE"/logs/catalina.out#CATALINA_OUT="$CATALINA_BASE"/logs/catalina.out.%Y-%m-%d#g' catalina.sh
                sed -i 's#org.apache.catalina.startup.Bootstrap "$@" start #org.apache.catalina.startup.Bootstrap "$@" start 2>\&1#g' catalina.sh
                sed -i 's#>> "$CATALINA_OUT" 2>&1 "&"#| /usr/local/sbin/cronolog "$CATALINA_OUT" >> /dev/null \&#g' catalina.sh
                echo "------change file finish--------"
        else
                echo "The $WEBDIR is not exist"
        fi

}

install
alterConf

