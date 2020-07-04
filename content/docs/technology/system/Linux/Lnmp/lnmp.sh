#!/bin/bash
#
#Desciption:The script is about install Tengine,mysql and PHP.
#
#Written by CC  --2015/11/26
#

NVERSION="tengine-2.1.1"
MVERSION="mysql-5.7.9"
PVERSION="php-5.6.15"
PACKAGEPATH="/usr/local/src/lnmp"
RETVAL=0

cd $PACKAGEPATH

function readInfo() { 
	echo -n "Install DIR for Nginx [/usr/local/nginx]："
	read NDIR
	echo -n "Install DIR for Mysql [/usr/local/mysql]："
	read MDIR
	echo -n "Install DIR for Mysql Data [/usr/local/mysql/data]："
	read DATADIR
	echo -n "Install DIR for PHP [/usr/local/php]："
	read PDIR
}

function yumInstall() {
	echo "yum install rely on package for nginx"
	sleep 5
	yum -y install gcc gcc-c++ autoconf automake zlib zlib-devel pcre-devel 2
	echo "yum install rely on package for mysql"
	sleep 5
	yum -y install cmake ncurses ncurses-devel
	echo "yum install rely on package for PHP"
	yum install -y libxml2-devel openssl-devel libcurl-devel libjpeg-devel freetype-devel libpng-devel libicu-devel openldap-devel bzip2-devel readline-devel php-gd 
}
function tarPackage() {
	tar -zxvf $NVERSION.tar.gz >>/dev/null 2>&1
	tar -zxvf $MVERSION.tar.gz >>/dev/null 2>&1
	tar -zxvf $PVERSION.tar.gz >>/dev/null 2>&1
}

function nginxInstall() {
	cd $PACKAGEPATH/$NVERSION
	./configure --prefix=$NDIR 2>&1 >> /usr/local/src/lnmp/nginx.log
	RETVAL=$?
	if [ $RETVAL -eq 0 ];then
		make && make install 2>&1 >> /usr/local/src/lnmp/nginx.log
		if [ -d $NDIR ];then
       	 	echo "The Nginx is install sucessful"
    	else
        	echo "Something Wrong,please find nginx.log to check!"
			exit 778 
    	fi
	else
		echo "Something Wrong,please find nginx.log to check!"
		exit 777
	fi
}

function mysqlInstall() {
	cd $PACKAGEPATH/$MVERSION
	USERS=$(cat /etc/passwd | awk -F':' '{print $1}' | grep mysql)
	if [ -z "$USERS" ];then
		chattr -i /etc/passwd /etc/shadow /etc/group /etc/gshadow
		groupadd mysql
		useradd -r -g mysql mysql
		chattr +i /etc/passwd /etc/shadow /etc/group /etc/gshadow
	fi
	
	cmake -DCMAKE_INSTALL_PREFIX=$MDIR -DDEFAULT_CHARSET=utf8 -DDEFAULT_COLLATION=utf8_general_ci -DDOWNLOAD_BOOST=1 -DWITH_BOOST=/usr/local/src/lnmp -DWITH_INNOBASE_STORAGE_ENGINE=1 -DWITH_ARCHIVE_STORAGE_ENGINE=1 -DWITH_BLACKHOLE_STORAGE_ENGINE=1 -DMYSQL_DATADIR=$DATADIR -DMYSQL_TCP_PORT=3306 -DENABLE_DOWNLOADS=1  2>&1 >>/usr/local/src/lnmp/mysql.log
	
	RETVAL=$?
	if [ $RETVAL -eq 0 ];then
		make && make install 2>&1 >>/usr/local/src/lnmp/mysql.log
		RETVAL=$?
		if [ $RETVAL -eq 0 ];then
			echo "----Install Mysql sucessful----"
		else
			echo "Something wrong,please find mysql.log to check!"
			exit 780
		fi
	else
		echo "Something wrong,please find mysql.log to check!"
		exit 779
	fi

	echo "$MDIR/lib" >> /etc/ld.so.conf.d/local.conf	
	echo "----initialize mysql----"
	if [ ! -d $DATADIR ];then
		mkdir -p $DATADIR
	fi
	$MDIR/bin/mysqld --initialize-insecure --user=mysql --basedir=$MDIR --datadir=$DATADIR 2>&1 >>/usr/local/src/lnmp/mysql.log
	cp $PACKAGEPATH/my.cnf $PACKAGEPATH/my.cnf.new
	sed -i "s@/usr/local/mysql@$MDIR@g" $PACKAGEPATH/my.cnf.new
	sed -i "s@/data/mysql@$DATADIR@g" $PACKAGEPATH/my.cnf.new	
	mv $PACKAGEPATH/my.cnf.new /etc/my.cnf
	/bin/cp $MDIR/support-files/mysql.server /etc/init.d/mysqld
	chmod +x /etc/init.d/mysqld
	/etc/init.d/mysqld start
}

function phpInstall() {
	cd $PACKAGEPATH
	USERS=$(cat /etc/passwd | awk -F':' '{print $1}' | grep www)
    if [ -z "$USERS" ] ;then
        chattr -i /etc/passwd /etc/shadow /etc/group /etc/gshadow
        groupadd www
        useradd -g www -s /sbin/nologin -M www
		chattr +i /etc/passwd /etc/shadow /etc/group /etc/gshadow
    fi

	which re2c
	RETVAL=$?
	if [ $RETVAL -ne 0 ];then	
		wget http://sourceforge.net/projects/re2c/files/0.15.3/re2c-0.15.3.tar.gz/download
        tar zxf re2c-0.15.3.tar.gz && cd re2c-0.15.3
		./configure
		make && make install
		cd $PACKAGEPATH
	fi

	
	MCRYPTPATH=$(find /usr -name "mcrypt.h")
	if [ -z "$MCRYPTPATH" ];then
		wget http://sourceforge.net/projects/mcrypt/files/Libmcrypt/2.5.8/libmcrypt-2.5.8.tar.gz
		tar -zxf libmcrypt-2.5.8.tar.gz && cd libmcrypt-2.5.8
		./configure
		make && make install
		echo "/usr/local/lib" >> /etc/ld.so.conf.d/local.conf 
		echo "/usr/local/lib64" >> /etc/ld.so.conf.d/local.conf 
		cd $PACKAGEPATH
	fi
	
	cd $PACKAGEPATH/$PVERSION	
	./configure --prefix=$PDIR --with-config-file-path=$PDIR/etc --enable-inline-optimization --disable-debug --disable-rpath --enable-shared --enable-opcache --enable-fpm --with-fpm-user=www --with-fpm-group=www --with-gd --with-jpeg-dir --with-freetype-dir --with-mysql=mysqlnd --with-mysqli=mysqlnd --with-pdo-mysql=mysqlnd --with-gettext --enable-mbstring --with-iconv --with-mcrypt --with-mhash --with-openssl --enable-bcmath --enable-soap --with-libxml-dir --enable-pcntl --enable-shmop --enable-sysvmsg --enable-sysvsem --enable-sysvshm --enable-sockets --with-curl --with-zlib --enable-zip --with-bz2 --with-readline  2>&1 >>/usr/local/src/lnmp/php.log
	
	RETVAL=$?
	if [ $RETVAL -eq 0 ];then
        make && make install 2>&1 >>/usr/local/src/lnmp/php.log
        RETVAL=$?
        if [ $RETVAL -eq 0 ];then
            echo "----Install PHP sucessful----"
        else
            echo "Something wrong,please find php.log to check!"
            exit 782
        fi
    else
        echo "Something wrong,please find php.log to check!"
        exit 781
    fi
	
	cp php.ini-development $PDIR/etc/php.ini
	cp sapi/fpm/init.d.php-fpm /etc/init.d/php-fpm
	cp $PDIR/etc/php-fpm.conf.default $PDIR/etc/php-fpm.conf
	chmod +x /etc/init.d/php-fpm
	/etc/init.d/php-fpm start
}

function setPath() {
	#Mysql environmnet add
	echo "#Mysql environment" >> /etc/profile
    echo "export MYSQL_HOME=$MDIR" >> /etc/profile
	#PHP environment add
    echo "#PHP environment" >> /etc/profile
    echo "export PHP_HOME=$PDIR" >> /etc/profile
    echo 'export PATH=$MYSQL_HOME/bin:$PHP_HOME/bin:$PATH' >> /etc/profile
    source /etc/profile
}


echo -n "Are you want to use the default install path? (y|n)："
read CHOICE

if [ $CHOICE == "y" ];then
	echo "------Start install LNMP-----"
	NDIR="/usr/local/nginx"
	MDIR="/usr/local/mysql"
	DATADIR="/cache1/mysql/data"
	PDIR="/usr/local/php"
elif [ $CHOICE == "n" ];then
	readInfo
else
	echo "The value is wrong"
fi


yumInstall
tarPackage
nginxInstall
mysqlInstall
phpInstall
setPath
