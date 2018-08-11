#!/bin/bash
source /etc/profile

zkServer={{ work_dir }}/zookeeper-{{ zk_version }}/bin/zkServer.sh
zkCfg={{ dirs['conf_dir'][0] }}/zoo.cfg

function start(){
	PID=$(jps | grep -i QuorumPeerMain | awk '{print $1}')
	if [ -z "${PID}" ];then
		${zkServer} start ${zkCfg} &
	else
		echo "Zookeeper is running (pid $PID)"
	fi
}

function stop(){
	PID=$(jps | grep -i QuorumPeerMain | awk '{print $1}')
	[ -n "${PID}" ] && ${zkServer} stop ${zkCfg}
	sleep 5
	jps | grep -i QuorumPeerMain >/dev/null
	if [ $? -ne 0 ];then
		echo "Zookeeper is stoped"
	else
		kill -9 ${PID}
	fi
}

function status(){
	PID=$(jps | grep -i QuorumPeerMain | awk '{print $1}')
	[ -n "${PID}" ] && echo "Zookeeper is running (pid ${PID})" || echo "Zookeeper is stoped"
}

case $1 in
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
    sleep 3
    start
    ;;
  *)
    echo $"Usage: $0 {start|stop|restart|status}"
        echo "Example: sh $0 zk.sh status"
esac
