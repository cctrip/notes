---
bookCollapseSection: false
weight: 5
title: "Kubernetes 安装"
---

# 安装

## kubeadm快速部署kubernetes

### 环境搭建

* 环境准备

      #放开防火墙限制
      systemctl stop firewalld
      systemctl disable firewalld
      
      #更改内核参数
      echo 1 > /proc/sys/net/bridge/bridge-nf-call-ip6tables
      echo 1 > /proc/sys/net/bridge/bridge-nf-call-iptables
      
      #禁用SELINUX
      setenforce 0

* Docker安装

  参考[Docker安装](../Docker/docker.md)

      #开启iptables filter表中FOWARD链(Docker1.3开始已被禁用)
      iptables -P FORWARD ACCEPT
      
      #/etc/docker/daemon.json增加配置
      {
          "exec-opts": ["native.cgroupdriver=systemd"]
      }
      
      #重启Docker
      systemctl restart docker.service

* Kubeadm安装

      #添加repo配置
      cat <<EOF > /etc/yum.repos.d/kubernetes.repo
      [kubernetes]
      name=Kubernetes
      baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
      enabled=1
      gpgcheck=1
      repo_gpgcheck=1
      gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
              https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
      EOF
      
      #安装kubeadm,kubelet,kubectl
      yum install -y kubelet kubeadm kubectl
      systemctl enable kubelet && systemctl start kubelet

***


### Master node 初始化

* init

      kubeadm init --pod-network-cidr=10.244.0.0/16
      
      #记录join值
      kubeadm join --token <token> <master-ip>:<master-port>
      
      #配置KUBECONFIG环境参数
      export KUBECONFIG=/etc/kubernetes/admin.conf

* Pod Network安装

      mkdir -p ~/k8s/
      wget https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel-rbac.yml
      wget https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
      kubectl create -f kube-flannel-rbac.yml
      kubectl apply -f  kube-flannel.yml

***

### Node 加入 Master

    kubeadm join --token <token> <master-ip>:<master-port>

***

### kubectl操作

    #获取组件状态
    kubectl get cs
    
    #查看pod状态
    kubectl get pod --all-namespaces -o wide
    
    #部署应用

***

## 手动部署kubernetes高可用集群

## 环境准备

### 软件

* etcd

* docker

* kubernetes

  * kubelet

  * kube-proxy

  * kube-apiserver

  * kube-controller-manager

  * kube-scheduler

***

### 软件准备

* [Docker安装](../Docker/docker.md)

* 软件下载

      wget https://storage.googleapis.com/kubernetes-release/release/v1.6.9/kubernetes.tar.gz
      tar -zxvf kubernetes.tar.gz
      ./kubernetes/cluster/get-kube-binaries.sh
      
      wget https://github.com/coreos/etcd/releases/download/v3.2.6/etcd-v3.2.6-linux-amd64.tar.gz

***

### etcd高可用集群搭建

#### 安装cfssl

    go get -u github.com/cloudflare/cfssl/cmd/...

将在$GOPATH/bin下安装cfssl, cfssjosn, mkbundle等工具

#### CA证书和私钥

创建ca-config.json:

    {
      "signing": {
        "default": {
          "expiry": "87600h"
        },
        "profiles": {
          "frognew": {
            "usages": [
                "signing",
                "key encipherment",
                "server auth",
                "client auth"
            ],
            "expiry": "87600h"
          }
        }
      }
    }

创建CA证书签名请求配置ca-csr.json:

    {
      "CN": "frognew",
      "key": {
        "algo": "rsa",
        "size": 2048
      },
      "names": [
        {
          "C": "CN",
          "ST": "BeiJing",
          "L": "BeiJing",
          "O": "frognew",
          "OU": "cloudnative"
        }
      ]
    }

使用cfssl生成CA证书和私钥：

    cfssl gencert -initca ca-csr.json | cfssljson -bare ca

ca-key.pem和ca.pem需要保存，后边会用到

#### etcd证书和私钥

创建etcd证书签名请求配置etcd-csr.json:

    {
      "CN": "cctest",
      "hosts": [
        "127.0.0.1",
        "192.168.19.11",
        "192.168.19.12",
        "192.168.19.13",
        "node1",
        "node2",
        "node3"
      ],
      "key": {
          "algo": "rsa",
          "size": 2048
      },
      "names": [
          {
              "C": "CN",
              "ST": "BeiJing",
              "L": "BeiJing",
              "O": "cctest",
              "OU": "cloudnative"
          }
      ]
    }

生成etcd的证书和私钥

    cfssl gencert -ca=ca.pem -ca-key=ca-key.pem -config=ca-config.json -profile=frognew etcd-csr.json | cfssljson -bare etcd

#### etcd安装

将ca.pem, etcd-key.pem, etcd.pem拷贝到各节点的/etc/etcd/ssl目录中

    cp ca.pem /etc/etcd/ssl
    cp etcd*.pem /etc/etcd/ssl

解压缩etcd-v3.2.6-linux-amd64.tar.gz，拷贝可执行文件

    tar -zxvf etcd-v3.2.6-linux-amd64.tar.gz
    cp etcd-v3.2.6-linux-amd64/etcd* /usr/bin/


创建etcd的systemd unit文件

    export ETCD_NAME=node1
    export INTERNAL_IP=192.168.19.11
    cat > /usr/lib/systemd/system/etcd.service <<EOF
    [Unit]
    Description=etcd server
    After=network.target
    After=network-online.target
    Wants=network-online.target
    
    [Service]
    Type=notify
    WorkingDirectory=/var/lib/etcd/
    EnvironmentFile=-/etc/etcd/etcd.conf
    ExecStart=/usr/bin/etcd \
      --name ${ETCD_NAME} \
      --cert-file=/etc/etcd/ssl/etcd.pem \
      --key-file=/etc/etcd/ssl/etcd-key.pem \
      --peer-cert-file=/etc/etcd/ssl/etcd.pem \
      --peer-key-file=/etc/etcd/ssl/etcd-key.pem \
      --trusted-ca-file=/etc/etcd/ssl/ca.pem \
      --peer-trusted-ca-file=/etc/etcd/ssl/ca.pem \
      --initial-advertise-peer-urls https://${INTERNAL_IP}:2380 \
      --listen-peer-urls https://${INTERNAL_IP}:2380 \
      --listen-client-urls https://${INTERNAL_IP}:2379,https://127.0.0.1:2379 \
      --advertise-client-urls https://${INTERNAL_IP}:2379 \
      --initial-cluster-token etcd-cluster-1 \
      --initial-cluster node1=https://192.168.19.11:2380,node2=https://192.168.19.12:2380,node3=https://192.168.19.13:2380 \
      --initial-cluster-state new \
      --data-dir=/var/lib/etcd
    Restart=on-failure
    RestartSec=5
    LimitNOFILE=65536
    
    [Install]
    WantedBy=multi-user.target
    EOF

#### 启动etcd

各节点启动etcd服务

    systemctl daemon-reload
    systemctl enable etcd
    systemctl start etcd
    systemctl status etcd

集群检查：

    etcdctl \
      --ca-file=/etc/etcd/ssl/ca.pem \
      --cert-file=/etc/etcd/ssl/etcd.pem \
      --key-file=/etc/etcd/ssl/etcd-key.pem \
      --endpoints=https://node1:2379,https://node2:2379,https://node3:2379 \
      cluster-health 

***

### Kubernetes Master 集群搭建

