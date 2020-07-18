---
bookCollapseSection: false
weight: 1
title: "Kubernetes Pod"
---

# Kubernetes Pod

## What

*Pod* 是 Kubernetes 应用程序的基本执行单元，即它是 Kubernetes 对象模型中创建或部署的最小和最简单的单元。Pod 表示在 [集群](https://kubernetes.io/zh/docs/reference/glossary/?all=true#term-cluster) 上运行的进程。

Pod 封装了应用程序容器（或者在某些情况下封装多个容器）、存储资源、唯一网络 IP 以及控制容器应该如何运行的选项。 Pod 表示部署单元：*Kubernetes 中应用程序的单个实例*，它可能由单个 [容器](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/#why-containers) 或少量紧密耦合并共享资源的容器组成。

[Docker](https://www.docker.com/) 是 Kubernetes Pod 中最常用的容器运行时，但 Pod 也能支持其他的[容器运行时](https://kubernetes.io/docs/setup/production-environment/container-runtimes/)。

Kubernetes 集群中的 Pod 可被用于以下两个主要用途：

- **运行单个容器的 Pod**。"每个 Pod 一个容器"模型是最常见的 Kubernetes 用例；在这种情况下，可以将 Pod 看作单个容器的包装器，并且 Kubernetes 直接管理 Pod，而不是容器。
- **运行多个协同工作的容器的 Pod**。 Pod 可能封装由多个紧密耦合且需要共享资源的共处容器组成的应用程序。 这些位于同一位置的容器可能形成单个内聚的服务单元 —— 一个容器将文件从共享卷提供给公众，而另一个单独的“挂斗”（sidecar）容器则刷新或更新这些文件。 Pod 将这些容器和存储资源打包为一个可管理的实体。 [Kubernetes 博客](https://kubernetes.io/blog) 上有一些其他的 Pod 用例信息。更多信息请参考：

- [分布式系统工具包：容器组合的模式](https://kubernetes.io/blog/2015/06/the-distributed-system-toolkit-patterns)
- [容器设计模式](https://kubernetes.io/blog/2016/06/container-design-patterns)

每个 Pod 表示运行给定应用程序的单个实例。如果希望横向扩展应用程序（例如，运行多个实例），则应该使用多个 Pod，每个应用实例使用一个 Pod 。在 Kubernetes 中，这通常被称为 *副本*。通常使用一个称为控制器的抽象来创建和管理一组副本 Pod。更多信息请参见 [Pod 和控制器](https://kubernetes.io/zh/docs/concepts/workloads/pods/pod-overview/#pods-and-controllers)。

***

## How

Pod 被设计成支持形成内聚服务单元的多个协作过程（作为容器）。 Pod 中的容器被自动的安排到集群中的同一物理或虚拟机上，并可以一起进行调度。 容器可以共享资源和依赖、彼此通信、协调何时以及何种方式终止它们。

注意，在单个 Pod 中将多个并置和共同管理的容器分组是一个相对高级的使用方式。 只在容器紧密耦合的特定实例中使用此模式。 例如，您可能有一个充当共享卷中文件的 Web 服务器的容器，以及一个单独的 sidecar 容器，该容器从远端更新这些文件，如下图所示：

![Pod 图例](https://d33wubrfki0l68.cloudfront.net/aecab1f649bc640ebef1f05581bfcc91a48038c4/728d6/images/docs/pod.svg)

有些 Pod 具有 [初始容器](https://kubernetes.io/zh/docs/reference/glossary/?all=true#term-init-container) 和 [应用容器](https://kubernetes.io/zh/docs/reference/glossary/?all=true#term-app-container)。初始容器会在启动应用容器之前运行并完成。

Pod 为其组成容器提供了两种共享资源：*网络* 和 *存储*。

#### 网络

每个 Pod 分配一个唯一的 IP 地址。 Pod 中的每个容器共享网络命名空间，包括 IP 地址和网络端口。 *Pod 内的容器* 可以使用 `localhost` 互相通信。 当 Pod 中的容器与 *Pod 之外* 的实体通信时，它们必须协调如何使用共享的网络资源（例如端口）。

#### 存储

一个 Pod 可以指定一组共享存储[卷](https://kubernetes.io/docs/concepts/storage/volumes/)。 Pod 中的所有容器都可以访问共享卷，允许这些容器共享数据。 卷还允许 Pod 中的持久数据保留下来，以防其中的容器需要重新启动。 有关 Kubernetes 如何在 Pod 中实现共享存储的更多信息，请参考[卷](https://kubernetes.io/docs/concepts/storage/volumes/)。

***

## Why

### 管理

Pod 是形成内聚服务单元的多个协作过程模式的模型。它们提供了一个比它们的应用组成集合更高级的抽象，从而简化了应用的部署和管理。Pod 可以用作部署、水平扩展和制作副本的最小单元。在 Pod 中，系统自动处理多个容器的在并置运行（协同调度）、生命期共享（例如，终止），协同复制、资源共享和依赖项管理。

### 资源共享和通信

Pod 使它的组成容器间能够进行数据共享和通信。

Pod 中的应用都使用相同的网络命名空间（相同 IP 和 端口空间），而且能够互相“发现”并使用 `localhost` 进行通信。因此，在 Pod 中的应用必须协调它们的端口使用情况。每个 Pod 在扁平的共享网络空间中具有一个 IP 地址，该空间通过网络与其他物理计算机和 Pod 进行全面通信。

Pod 中的容器获取的系统主机名与为 Pod 配置的 `name` 相同。[网络](https://kubernetes.io/docs/concepts/cluster-administration/networking/) 部分提供了更多有关此内容的信息。

Pod 除了定义了 Pod 中运行的应用程序容器之外，Pod 还指定了一组共享存储卷。该共享存储卷能使数据在容器重新启动后继续保留，并能在 Pod 内的应用程序之间共享。

***