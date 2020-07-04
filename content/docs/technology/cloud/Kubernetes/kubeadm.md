# kubeadm快速部署kubernetes

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

