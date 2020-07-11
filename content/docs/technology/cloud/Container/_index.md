---
bookCollapseSection: true
weight: 2
title: "容器技术"
---

# 容器技术

## What

### 定义

> 容器提供了一种逻辑打包机制，以这种机制打包的应用可以脱离其实际运行的环境。利用这种脱离，不管目标环境是私有数据中心、公有云，还是开发者的个人笔记本电脑，您都可以轻松、一致地部署基于容器的应用。容器化使开发者和 IT 运营团队的关注点泾渭分明 - 开发者专注于应用逻辑和依赖项，而 IT 运营团队可以专注于部署和管理，不必为应用细节分心，例如具体的软件版本和应用特有的配置。

***

### VM vs Container

![](containers.png)

***

## Why

与虚拟机的硬件堆栈虚拟化不同，容器在操作系统级别进行虚拟化，且可以直接在操作系统内核上运行多个容器。也就是说，容器更轻巧：它们共享操作系统内核，启动速度更快，且与启动整个操作系统相比其占用的内存微乎其微。

* **一致的环境**

* **在任何地方运行**

* **隔离**

  容器会在操作系统级别虚拟化 CPU、内存、存储和网络资源，为开发者提供在逻辑上与其他应用相隔离的沙盒化操作系统接口。

***

## How

### 基础

#### Namespaces

Namespace是对全局系统资源的一种封装隔离，使得处于不同namespace的进程拥有独立的全局系统资源，改变一个namespace中的系统资源只会影响当前namespace里的进程，对其他namespace中的进程没有影响。

目前，Linux内核里面实现了7种不同类型的namespace。

```markdown
名称         宏定义             隔离内容
Cgroup      CLONE_NEWCGROUP   Cgroup root directory (since Linux 4.6)
IPC         CLONE_NEWIPC      System V IPC, POSIX message queues (since Linux 2.6.19)
Network     CLONE_NEWNET      Network devices, stacks, ports, etc. (since Linux 2.6.24)
Mount       CLONE_NEWNS       Mount points (since Linux 2.4.19)
PID         CLONE_NEWPID      Process IDs (since Linux 2.6.24)
User        CLONE_NEWUSER     User and group IDs (started in Linux 2.6.23 and completed in Linux 3.8)
UTS         CLONE_NEWUTS      Hostname and NIS domain name (since Linux 2.6.19)
```

#### Control groups

cgroup和namespace类似，也是将进程进行分组，但它的目的和namespace不一样，namespace是为了隔离进程组之间的资源，而cgroup是为了对一组进程进行统一的资源监控和限制。

cgroup主要包括下面两部分：

* subsystem 

  一个subsystem就是一个内核模块，他被关联到一颗cgroup树之后，就会在树的每个节点（进程组）上做具体的操作。subsystem经常被称作"resource controller"，因为它主要被用来调度或者限制每个进程组的资源，但是这个说法不完全准确，因为有时我们将进程分组只是为了做一些监控，观察一下他们的状态，比如perf_event subsystem。到目前为止，Linux支持12种subsystem，比如限制CPU的使用时间，限制使用的内存，统计CPU的使用情况，冻结和恢复一组进程等。

* hierarchy 

  一个hierarchy可以理解为一棵cgroup树，树的每个节点就是一个进程组，每棵树都会与零到多个subsystem关联。在一颗树里面，会包含Linux系统中的所有进程，但每个进程只能属于一个节点（进程组）。系统中可以有很多颗cgroup树，每棵树都和不同的subsystem关联，一个进程可以属于多颗树，即一个进程可以属于多个进程组，只是这些进程组和不同的subsystem关联。目前Linux支持12种subsystem，如果不考虑不与任何subsystem关联的情况（systemd就属于这种情况），Linux里面最多可以建12颗cgroup树，每棵树关联一个subsystem，当然也可以只建一棵树，然后让这棵树关联所有的subsystem。当一颗cgroup树不和任何subsystem关联的时候，意味着这棵树只是将进程进行分组，至于要在分组的基础上做些什么，将由应用程序自己决定，systemd就是一个这样的例子。

#### Union file systems

容器中使用的文件系统是可堆叠的，这意味着可以将不同分支中的文件和目录重叠以形成单个文件系统。该系统有助于避免在每次部署新容器时重复数据。Docker使用此技术实现镜像的功能[文档](https://docs.docker.com/storage/storagedriver/)

* overlay2
* aufs

***

## 案例

### 容器技术实现

* [Docker](Docker)

***

### 容器编排与调度

* [Kubernetes](Kubernetes)

