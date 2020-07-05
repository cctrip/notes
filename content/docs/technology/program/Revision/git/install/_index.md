---
bookCollapseSection: false
weight: 1
title: "Git安装"
---

## Git安装

* yum安装
		
		$ sudo yum install git

* 源码安装

	依赖包安装

		$ sudo yum install curl-devel expat-devel gettext-devel openssl-devel zlib-devel asciidoc xmlto docbook2x

	从[https://www.kernel.org/pub/software/scm/git](https://www.kernel.org/pub/software/scm/git)获取最新的版本包

	编译安装

		$ tar -zxf git-2.0.0.tar.gz
  		$ cd git-2.0.0
  		$ make configure
  		$ ./configure --prefix=/usr/local/git
  		$ make all doc info
  		$ sudo make install install-doc install-html install-info
	
  	升级
	
  		$ git clone git://git.kernel.org/pub/scm/git/git.git

***

## Git初始配置

Git 自带一个 git config 的工具来帮助设置控制 Git 外观和行为的配置变量。 这些变量存储在三个不同的位置：

1. /etc/gitconfig 文件: 包含系统上每一个用户及他们仓库的通用配置。 如果使用带有 --system 选项的 git config 时，它会从此文件读写配置变量。

2. ~/.gitconfig 或 ~/.config/git/config 文件：只针对当前用户。 可以传递 --global 选项让 Git 读写此文件。

3. 当前使用仓库的 Git 目录中的 config 文件（就是 .git/config）：针对该仓库。

每一个级别覆盖上一级别的配置，所以 .git/config 的配置变量会覆盖 /etc/gitconfig 中的配置变量。

#### 用户信息

当安装完 Git 应该做的第一件事就是设置你的用户名称与邮件地址。 这样做很重要，因为每一个 Git 的提交都会使用这些信息，并且它会写入到你的每一次提交中，不可更改：

	$ git config --global user.name "CodeCC"
	$ git config --global user.email CodeCC@example.com

再次强调，如果使用了 --global 选项，那么该命令只需要运行一次，因为之后无论你在该系统上做任何事情， Git 都会使用那些信息。 当你想针对特定项目使用不同的用户名称与邮件地址时，可以在那个项目目录下运行没有 --global 选项的命令来配置。

很多 GUI 工具都会在第一次运行时帮助你配置这些信息。


#### 检查配置信息

如果想要检查你的配置，可以使用 git config --list 命令来列出所有 Git 当时能找到的配置。

	$ git config --list
	user.name=CodeCC
	user.email=CodeCC@example.com
	...

也可以通过输入 git config <key>： 来检查 Git 的某一项配置

	$ git config user.name
	CodeCC

