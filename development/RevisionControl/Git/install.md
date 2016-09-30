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