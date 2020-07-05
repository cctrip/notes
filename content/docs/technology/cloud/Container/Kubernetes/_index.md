---
bookCollapseSection: true
weight: 2
title: "K8S"
---

# Kubernetes

k8s是一个开源系统，它可以被用于自动部署，扩展和管理容器化（containerized）应用程序。

***

### 架构

![k8s架构](architecture.png)

***

##### Master

* etcd

* API Server

* Scheduler

* Controller manager

##### Node

* Kubelet

* Kube-proxy

* cAdvisor

***

### 安装

* [Kubeadm](kubeadm.md)

    基于kubeadm工具部署kubernetes,包含Master和Node。(测试版本，不适用于生产环境)

* [Master-Cluster](cluster.md)

    基于kubernetes安装包部署kubernetes集群环境。

***

### Objects


#### basic objects

* Pod

* Service

* Volume

* Namespace

#### controllers

基于basic objects，提供额外的功能。

* ReplicaSet

* Deployment

* StatefulSet

* DaemonSet

* Job

***

### Control Plane

* Kubernetes Master

* Kubernetes Nodes