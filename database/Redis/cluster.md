## 集群

### 集群搭建

* Redis安装

        wget http://download.redis.io/releases/redis-3.2.6.tar.gz

* 基础配置

        #除端口外，配置统一
        port 6379
        cluster-enabled yes
        cluster-config-file nodes.conf
        cluster-node-timeout 5000
        appendonly yes

* redis集群架构

        192.168.88.1:6379(master) 192.168.88.2:6379(slave)
        192.168.88.2:6378(master) 192.168.88.3:6378(slave)
        192.168.88.3:6377(master) 192.168.88.1:6377(slave)

* 启动redis

        cd $PATH
        redis-server redis-6379.conf &

* 集群管理器安装

        #安装ruby        
        tar -zxf ruby-2.4.0.tar.gz
        cd ruby-2.4.0
        ./configure
        make && make install
        
        #安装gem
        tar -zxf rubygems-2.6.8.tgz
        cd rubygems-2.6.8/
        ruby setup.rb --no-rdoc --no-ri
        
        #安装redisgem
        gem install redis-3.3.3.gem --local --no-rdoc --no-ri

* 集群建立

        cd /usr/local/src/redis-3.2.6/
        src/redis-trib.rb create --replicas 1 172.16.88.1:6379 172.16.88.2:6378 172.16.88.3:6377 172.16.88.2:6379 172.16.88.3:6378 172.16.88.1:6377

* 简单测试

        redis-cli -c -h 172.16.88.1 -p 6379 cluster nodes

* 集群分片

        src/redis-trib.rb reshard 172.16.88.1:6379

* 添加节点

        src/redis-trib.rb add-node 172.16.88.1:6376 172.16.88.1:6379
        src/redis-trib.rb add-node --slave --master-id xxxx 172.16.88.1:6376 172.16.88.1:6379

* 从节点更改

        redis-cli -c -p 6377 cluster replicate <master-node-id>

***

### 集群优化

* 配置文件优化
* 集群配置密码
