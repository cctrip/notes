# Zookeeper部署

### 单机环境搭建


* 下载安装包

        wget http://mirror.bit.edu.cn/apache/zookeeper/zookeeper-3.4.10/zookeeper-3.4.10.tar.gz
        tar -zxvf zookeeper-3.4.10.tar.gz
        mv zookeeper-3.4.10 zookeeper

* 修改配置文件

        #vim zookeeper/conf/zoo.cfg
        tickTime=2000
        initLimit=5
        syncLimit=2
        dataDir=/cache1/zookeeper/data  #数据目录
        clientPort=2181                 #服务端口

* 配置日志保存目录

        #修改zookeeper/conf/log4j.properties文件
        zookeeper.root.logger=INFO, ROLLINGFILE
        zookeeper.log.dir=/cache1/zookeeper/logs
        zookeeper.log.file=zookeeper.log

        #修改zookeeper/bin/zkEnv.sh
        if [ "x${ZOO_LOG_DIR}" = "x" ]
        then
            ZOO_LOG_DIR="/cache1/zookeeper/logs/"
        fi

        if [ "x${ZOO_LOG4J_PROP}" = "x" ]
        then
            ZOO_LOG4J_PROP="INFO,ROLLINGFILE"
        fi

* 启动服务

        cd zookeeper/bin && ./zkServer.sh start

***

### 集群环境搭建

* 机器准备

        #3台设备
        192.168.1.21
        192.168.1.22
        192.168.1.33

* 系统环境准备

        #/etc/hosts文件增加以下内容
        192.168.1.21 zoo1
        192.168.1.22 zoo2
        192.168.1.33 zoo3

* 下载安装包

        wget http://mirror.bit.edu.cn/apache/zookeeper/zookeeper-3.4.10/zookeeper-3.4.10.tar.gz
        tar -zxvf zookeeper-3.4.10.tar.gz
        mv zookeeper-3.4.10 zookeeper

* 修改配置文件

        #vim zookeeper/conf/zoo.cfg
        tickTime=2000
        initLimit=5
        syncLimit=2
        dataDir=/cache1/zookeeper/data  #数据目录
        clientPort=2181                 #服务端口
        server.1=zoo1:2888:3888         #server.x的x与myid文件的值匹配
        server.2=zoo2:2888:3888         #zoo1表示hostname
        server.3=zoo3:2888:3888         #2888是followers用来连接leader，3888用于leader的选举

* 各机器创建myid文件

        #zoo1
        echo 1 > /cache1/zookeeper/data/myid

        #zoo2
        echo 2 > /cache1/zookeeper/data/myid

        #zoo3
        echo 3 > /cache1/zookeeper/data/myid

* 各机器启动服务

        cd zookeeper/bin && ./zkServer.sh start
