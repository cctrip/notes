---
bookCollapseSection: true
weight: 2
title: "Docker"
---

# Docker

## What

> Docker是一个用于开发，交付和运行应用程序的开放平台。 Docker使您能够将应用程序与基础架构分开，从而可以快速交付软件。 借助Docker，您可以以与管理应用程序相同的方式来管理基础架构。

***

### Docker平台

Docker提供了在松散隔离的环境（称为容器）中打包和运行应用程序的功能。隔离和安全性使您可以在给定主机上同时运行多个容器。容器重量轻，因为它们不需要管理程序的额外负担，而是直接在主机的内核中运行。这意味着与使用虚拟机相比，可以在给定的硬件组合上运行更多的容器。您甚至可以在实际上是虚拟机的主机中运行Docker容器！

Docker提供了工具和平台来管理容器的生命周期：

* 使用容器开发应用程序及其支持组件。
* 容器成为分发和测试您的应用程序的单元。
* 准备就绪后，可以将应用程序作为容器或协调服务部署到生产环境中。无论您的生产环境是本地数据中心，云提供商还是二者的混合体，其工作原理都相同。

***

### Docker Engine

Docker Engine是具有这些主要组件的client-server应用程序：

* `Docker daemon`是一个长时间运行的守护进程
* `REST API`指定程序可以用来与守护程序进行通信并指示其操作的接口
* `command line interface (CLI)` 客户端

`CLI`使用`Docker REST API`通过脚本或直接`CLI`命令来控制`Docker守护程序`或与`Docker守护程序`进行交互。许多其他Docker应用程序都使用基础API和CLI。

`Docker daemon `创建和管理Docker对象，例如映像，容器，网络和卷。

![](engine-components-flow.png)

***

## How

### [架构](arch)

![](architecture.svg)

***

### [底层技术](under)

#### [Namespaces](under/namespace)

Namespace实现对全局系统资源的一种封装隔离

#### [Control Groups](under/cgroup)

CGroup是为了对一组进程进行统一的资源监控和限制

#### [Union file systems](under/uninofs)

Union file system 实现将不同分支中的文件和目录重叠以形成单个文件系统。

#### Container format

Docker Engine将Namespace，CGroup和UnionFS组合到一个称为`container format`的包装器中。 默认容器格式为`libcontainer`。 将来，Docker可能会通过与BSD Jails或Solaris Zone等技术集成来支持其他容器格式。