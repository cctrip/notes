#!/bin/bash
#
#Written by: CC  --2015/10/20
#
if [ -r /lib/lsb/init-functions ];then
	. /lib/lsb/init-functions
else
	exit 1
fi


WEBPATH=/cache1/web
PROJECT=$1
RETVAL=0


function start(){
for pro in ${PROJECT[@]}
do
	PIDS=`ps -ef | grep java | grep $pro | awk '{print $2}'`
	if [ ! -z $PIDS ];then
		echo "The service $pro is started"
	else
		su -l webrunner -c "$WEBPATH/$pro/bin/startup.sh" 2>&1 > /dev/null
		RETVAL=$?
		if [ $RETVAL -eq 0 ];then
			log_success_msg "Starting $pro"
		else 
			log_failure_msg "Starting $pro"
		fi
	fi
done
}



function stop(){
for pro in ${PROJECT[@]}
do
	PIDS=`ps -ef | grep java | grep $pro | awk '{print $2}'`
	if [ -z $PIDS ];then
		echo "The service $pro is stoped"
	else
		echo -en "shutting down $pro \t..."
		su -l webrunner -c "$WEBPATH/$pro/bin/shutdown.sh" > /dev/null 2>&1
		sleep 3
		PIDS=`ps -ef | grep java | grep $pro | awk '{print $2}'`
		if [ -z $PIDS ];then
			log_success_msg 
		else
			kill -9 $PIDS
			RETVAL=$?
			if [ $RETVAL -eq 0 ];then
				log_success_msg
			else
				log_failure_msg
			fi
		fi
	fi
done
}


function status(){
for pro in ${PROJECT[@]}
do
	 PIDS=`ps -ef | grep java | grep $pro | awk '{print $2}'`
	 [ "$PIDS" == "" ] && log_success_msg "The service $pro is not running"
	 [ "$PIDS" != "" ] && log_success_msg "The service $pro($PIDS) is running"
done
}


case $2 in
  start)
	start
	;;
  stop)
	stop
	;;
  status)
	status
	;;
  restart)
	stop
	start
	;;
  *)
	echo $"Usage: $0 CATALINA_BASE {start|stop|restart|status}"
    	echo "Example: sh $0 web-test status"
esac

