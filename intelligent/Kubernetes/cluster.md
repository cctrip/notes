# 手动部署kubernetes高可用集群

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

