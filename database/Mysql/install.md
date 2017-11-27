# Mysql 安装

### 源码编译安装

#### 准备

* CMake(build framework)

      yum -y install cmake

* GNU make(make program)

      yum -y install make

* GCC(ANSI C++ complier)
    
      yum -y install gcc gcc-c++

* Boost C++ libraries

* ncurses library

      yum -y install ncurses ncurses-devel

* Perl(run test scripts)

      yum -y install perl

***

#### 安装

* 创建用户组

      shell> groupadd mysql
      shell> useradd -r -g mysql -s /bin/false mysql

* 编译安装

      shell> tar -zxvf mysql-VERSION.tar.gz
      shell> cd mysql-VERSION
      shell> mkdir bld
      shell> cd bld
      shell> cmake .. -DDOWNLOAD_BOOST=1 -DWITH_BOOST=/usr/local/src -DCMAKE_INSTALL_PREFIX=/cache1/mysql -DDEFAULT_CHARSET=utf8 -DDEFAULT_COLLATION=utf8_general_ci
      shell> make
      shell> make install

* 数据初始化

/etc/my.cnf文件配置

    [client]
    port=3306
    socket=/tmp/mysql.sock

    [mysqld]
    port=3306
    socket=/tmp/mysql.sock
    datadir=/cache1/mysql/data
    symbolic-links=0
    log-error=/cache1/mysql/log/mysqld.log
    pid-file=/cache1/mysql/log/mysqld.pid

数据初始化

    shell> cd /cache1/mysql
    shell> mkdir data log
    shell> chown -R mysql:mysql data
    shell> chown -R mysql:mysql log
    shell> bin/mysqld --initialize --user=mysql
    shell> cp support-files/mysql.service /etc/init.d/mysqld
    shell> /etc/init.d/mysqld start
    shell> mysql -uroot -p

    mysql> ALTER USER user IDENTIFIED BY 'new_password';
    mysql> SELECT User, Host, HEX(authentication_string) FROM mysql.user;




