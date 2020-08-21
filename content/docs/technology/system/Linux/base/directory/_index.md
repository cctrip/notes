---
bookCollapseSection: false
weight: 2
title: "目录结构"
---

# Linux目录结构

* /boot

  系统启动相关的文件，如内核、initrd，以及grub(bootloader)

* /dev

    设备文件

    块设备：随机访问，数据块

    字符设备：线性访问，按字符为单位

    设备号：主设备号(major)和次设备号(minor)

* /etc

  配置文件

* /home

  用户的家目录，每一个用户的家目录通常默认为/home/USERNAME

* /root

    管理员的家目录

* /lib

    库文件

    静态库，.a
    
    动态库，.dll，.so（shared object）

* /lib/modules

    内核模块文件

* /media

    挂载点目录，移动设备

* /mnt

    挂载点目录，额外的临时文件系统

* /opt

    可选目录，第三方程序的安装目录

* /proc

  伪文件系统，内核映射文件

* /sys

  伪文件系统，跟硬件设备相关的属性映射文件

* /tmp

  临时文件，/var/tmp

* /var

  可变化的文件

* /bin

  可执行文件，用户命令

* /sbin

  可执行文件，管理命令

* /usr

  shared，read-only

  /usr/bin

  /usr/sbin

  /usr/lib

* /usr/local

  第三方软件

  /usr/local/bin

  /usr/local/sbin

  /usr/local/lib

***
