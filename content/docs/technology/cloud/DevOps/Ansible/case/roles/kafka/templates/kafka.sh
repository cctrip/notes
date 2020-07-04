#!/bin/bash
source /etc/profile

export KAFKA_LOG4J_OPTS="-Dlog4j.configuration=file:/etc/kafka/log4j.properties"
export LOG_DIR="{{ dirs['log_dir'][0] }}"

kafkaServerStart={{ work_dir }}/kafka_{{ kafka_version }}/bin/kafka-server-start.sh
kafkaCfg={{ dirs['conf_dir'][0] }}/server.properties

function start(){
	PID=$(jps | grep -i Kafka | awk '{print $1}')
	if [ -z "${PID}" ];then
		echo "Starting Kafka..."
		${kafkaServerStart}  ${kafkaCfg} > /dev/null 2>&1 &
		sleep 5
		PID=$(jps | grep -i Kafka | awk '{print $1}')
		[ -n "${PID}" ] && echo "started ($PID)"
	else
		echo "Kafka is running (pid $PID)"
	fi
}

function stop(){
	PID=$(jps | grep -i Kafka | awk '{print $1}')
	[ -n "${PID}" ] && echo "Stoping Kafka, wait. " && kill -9 ${PID} 
	sleep 1
	jps | grep -i Kafka >/dev/null
	if [ $? -ne 0 ];then
		echo ".Stoped"
	else
		kill -9 ${PID} && echo ".Stoped"
	fi
}

function status(){
	PID=$(jps | grep -i Kafka | awk '{print $1}')
	[ -n "${PID}" ] && echo "Kafka is running (pid ${PID})" || echo "Kafka is stoped"
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
