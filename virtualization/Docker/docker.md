# Docker

容器，操作系统层面的虚拟化技术。

***

### 基本概念

* [镜像]()

* [容器]()

* [仓库]()

***

### 安装

Docker安装

    #删除旧版本
    yum remove docker docker-common docker-selinux docker-engine

    #获取repository文件
    yum install -y yum-utils device-mapper-persistent-data lvm2
    yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

    #安装新版本
    yum install docker-ce

    #启动
    systemctl start docker.service

***

### 基本使用

* docker pull <ImageName>:<version>  
    获取镜像

* docker run [options] <ImageName>:<version>
    options
    * -v <local_dir>:<container_dir>
    * -p <local_port>:<container_port>
    * -i
    * -d

* docker ps 查看容器

* docker images  查看镜像

***

### Dockerfile

Dockerfile编写

    FROM <imagename>:<version>   #基于某个镜像

    ENV <key> <value>            #设置环境变量

    RUN command                  #执行命令

    COPY <local_file> <container_path> #拷贝本地文件到容器

    CMD

***