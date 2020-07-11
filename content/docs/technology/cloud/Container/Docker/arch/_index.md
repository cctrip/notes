---
bookCollapseSection: false
weight: 2
title: "架构"
---

# 架构

## 组件

![](../architecture.svg)

***

### Docker daemon

`Docker daemon (dockerd)` 监听Docker API请求并管理Docker对象，例如图像，容器，网络和卷。 守护程序还可以与其他守护程序通信以管理Docker服务。

### Docker client

`Docker client (docker)` 是许多Docker用户与Docker交互的主要方式。 当您使用诸如docker run之类的命令时，客户端会将这些命令发送至dockerd，后者将其执行。 docker命令使用Docker API。 Docker客户端可以与多个守护程序通信。

### Docker registries

`Docker registry`存储Docker映像。 Docker Hub是任何人都可以使用的公共注册表，并且Docker配置为默认在Docker Hub上查找映像。 您甚至可以运行自己的私人注册表。

当使用 `docker pull` or `docker run` 命令时, 将从配置的registry中拉去镜像，当使用 `docker push` 命令时，镜像将被推送到配置的registry中 。

### Docker objects

使用Docker时，您正在创建和使用映像，容器，网络，卷，插件和其他对象。 本节是其中一些对象的简要概述。

#### IMAGES

`Image`是一个只读模板，其中包含创建Docker容器的说明。 通常，一个图像*基于*另一个图像，并带有一些附加的自定义。 例如，您可以基于“ ubuntu”映像构建映像，但安装Apache Web服务器和您的应用程序以及运行应用程序所需的配置详细信息。

您可以创建自己的图像，也可以仅使用其他人创建并在注册表中发布的图像。 要构建自己的映像，您可以使用简单的语法创建*Dockerfile*，以定义创建映像和运行映像所需的步骤。 Dockerfile中的每条指令都会在映像中创建一个层。 当您更改Dockerfile并重建映像时，仅重建那些已更改的层。 与其他虚拟化技术相比，这是使映像如此轻巧，小型和快速的部分原因。

#### CONTAINERS

`Container`是image的可运行实例。 您可以使用Docker API或CLI创建，启动，停止，移动或删除容器。 您可以将容器连接到一个或多个网络，将存储连接到它，甚至根据其当前状态创建一个新映像。

默认情况下，容器与其他容器及其主机之间的隔离度相对较高。 您可以控制容器的网络，存储或其他基础子系统与其他容器或主机之间的隔离程度。

容器由其映像以及在创建或启动时为其提供的任何配置选项定义。 删除容器后，未存储在永久性存储中的状态更改将消失。

#### SERVICES

`Service`使您可以在多个Docker守护程序之间扩展容器，这些守护程序都可以与多个*managers*和*workers* 一起作为*swarm*协同工作。 群的每个成员都是Docker守护程序，所有守护程序都使用Docker API进行通信。 服务允许您定义所需的状态，例如在任何给定时间必须可用的服务副本数。 默认情况下，该服务在所有工作节点之间是负载平衡的。 对于消费者而言，Docker服务似乎是一个单独的应用程序。 Docker Engine在Docker 1.12及更高版本中支持集群模式。

***