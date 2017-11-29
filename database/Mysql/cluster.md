# MySQL Cluster 


### Master-Slave

#### Master配置
/etc/my.cnf 增加配置
    
    [mysqld]
    server-id=1
    log-bin=/cache1/mysql/log/mysql-bin.log
    #忽略系统库
    binlog-ignore-db=mysql
    binlog-ignore-db=information_schema
    binlog-ignore-db=performance_schema
    
Replication 帐号创建

    mysql> GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%' IDENTIFIED BY 'slave@2017';

导出数据到从库
    
    mysql> USE newdatabase;
    mysql> FLUSH TABLES WITH READ LOCK;
    mysql> SHOW MASTER STATUS;
    +------------------+----------+--------------+---------------------------------------------+-------------------+
    | File             | Position | Binlog_Do_DB | Binlog_Ignore_DB                            | Executed_Gtid_Set |
    +------------------+----------+--------------+---------------------------------------------+-------------------+
    | mysql-bin.000002 |      754 |              | mysql,information_schema,performance_schema |                   |
    +------------------+----------+--------------+---------------------------------------------+-------------------+
    1 row in set (0.00 sec)

    shell> mysqldump -u root -p --opt newdatabase > newdatabase.sql

    mysql> UNLOCK TABLES;

#### Slave配置
/etc/my.cnf增加配置
    
    [mysqld]
    server-id=2
    log-bin=/cache1/mysql/log/mysql-bin.log
    #忽略系统库
    binlog-ignore-db=mysql
    binlog-ignore-db=information_schema
    binlog-ignore-db=performance_schema

导入数据

    mysql> CREATE DATABASE newdatabase;

    shell> mysql -u root -p newdatabase < /path/to/newdatabase.sql

配置主服务器

    mysql> CHANGE MASTER TO MASTER_HOST='master_host_name',MASTER_USER='repl',MASTER_PASSWORD='slave@2017',MASTER_LOG_FILE='mysql-bin.000002',MASTER_LOG_POS=754;
    mysql> START SLAVE;
    mysql> SHOW SLAVE STATUS\G;

***

### Master-Master

#### Master1，Master2配置
/etc/my.cnf 增加配置
    
    [mysqld]
    server-id=1
    log-bin=/cache1/mysql/log/mysql-bin.log
    #忽略系统库
    binlog-ignore-db=mysql
    binlog-ignore-db=information_schema
    binlog-ignore-db=performance_schema
    
Replication 帐号创建

    mysql> GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%' IDENTIFIED BY 'slave@2017';


#### Master1查看本机Master状态

    mysql> SHOW MASTER STATUS;
    +------------------+----------+--------------+---------------------------------------------+-------------------+
    | File             | Position | Binlog_Do_DB | Binlog_Ignore_DB                            | Executed_Gtid_Set |
    +------------------+----------+--------------+---------------------------------------------+-------------------+
    | mysql-bin.000002 |      754 |              | mysql,information_schema,performance_schema |                   |
    +------------------+----------+--------------+---------------------------------------------+-------------------+
    1 row in set (0.00 sec)

#### Master2查看本机Master状态

    mysql> show master status;
    +------------------+----------+--------------+---------------------------------------------+-------------------+
    | File             | Position | Binlog_Do_DB | Binlog_Ignore_DB                            | Executed_Gtid_Set |
    +------------------+----------+--------------+---------------------------------------------+-------------------+
    | mysql-bin.000001 |      915 |              | mysql,information_schema,performance_schema |                   |
    +------------------+----------+--------------+---------------------------------------------+-------------------+
    1 row in set (0.00 sec)

#### Master1配置成Master2的从库

    mysql> CHANGE MASTER TO MASTER_HOST='master2',MASTER_USER='repl',MASTER_PASSWORD='slave@2017',MASTER_LOG_FILE='mysql-bin.000001',MASTER_LOG_POS=915;
    mysql> START SLAVE;
    mysql> SHOW SLAVE STATUS\G;

#### Master2配置成Master1的从库

    mysql> CHANGE MASTER TO MASTER_HOST='master_host_name',MASTER_USER='repl',MASTER_PASSWORD='slave@2017',MASTER_LOG_FILE='mysql-bin.000002',MASTER_LOG_POS=754;
    mysql> START SLAVE;
    mysql> SHOW SLAVE STATUS\G;

***