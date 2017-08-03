# kubeadm快速部署kubernetes

### 环境准备

1. 关闭防火墙,或者开放访问端口

        systemctl stop firewalld
        systemctl disable firewalld

2. 更改内核参数

        echo 1 > /proc/sys/net/bridge/bridge-nf-call-ip6tables
        echo 1 > /proc/sys/net/bridge/bridge-nf-call-iptables

        #永久更改
        vim /etc/sysctl.d/k8s.conf 
        #添加内容
        net.bridge.bridge-nf-call-ip6tables = 1
        net.bridge.bridge-nf-call-iptables = 1

        sysctl -p /etc/sysctl.d/k8s.conf   #使配置生效

3. 禁用SELINUX

        setenforce 0

        vi /etc/selinux/config
        SELINUX=disabled

***

### 安装Docker

参考[Docker安装](../Docker/docker.md)

Docker从1.13版本开始调整了默认的防火墙规则，禁用了iptables filter表中FOWARD链，这样会引起Kubernetes集群中跨Node的Pod无法通信，在各个Docker节点执行下面的命令：

    iptables -P FORWARD ACCEPT

    #/etc/docker/daemon.json增加配置

    {
        "exec-opts": ["native.cgroupdriver=systemd"]
    }

    systemctl restart docker.service

***


### 安装kubeadm,kubelet,kubectl

各节点安装kubeadm,kubelet,kubectl

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

    yum install -y kubelet kubeadm kubectl
    systemctl enable kubelet && systemctl start kubelet

***

### kubeadm初始化

Master node 执行初始化

    kubeadm init --pod-network-cidr=10.244.0.0/16

***

### Pod Network安装

    mkdir -p ~/k8s/
    wget https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel-rbac.yml
    wget https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
    kubectl create -f kube-flannel-rbac.yml
    kubectl apply -f  kube-flannel.yml

*** 