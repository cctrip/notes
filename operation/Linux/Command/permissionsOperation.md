# 权限操作

### 权限

* 可读(r)(4)

* 可写(w)(2)

* 可执行(x)(1)

* 特殊权限

    * SUID(u+s): 运行某程序时，相应进程的属主是程序文件自身的属主

    * SGID(g+s)：运行某程序时，相应进程的属组是程序文件自身的属组

    * Sticky(o+t)：在一个公共目录，每个用户都可以创建删除自己的文件，但不能删除别人的文件

***

### 用户和组

* 用户(UID)

    * 类别

        * 管理员：0

        * 普通用户：1-65535

          * 系统用户：1-499

          * 一般用户：500-65535

    * 配置文件

        * /etc/passwd

          字段详解(以":"为分割符)
          
          用户名 : 密码 : UID : GID : 注释 : 家目录 : 默认shell

        * /etc/shadow

          字段详解(以":"为分隔符)

          用户名 : 密码 : 最近一次修改密码时间 : 最短使用期限 : 最长使用期限 : 警告时间 : 非活动时间 : 过期时间 

* 组(GID)

    * 类别

        * 私有组：创建用户时，没指定所组，则系统默认创建同名组

        * 基本组：用户的默认组

        * 附加组：

    * 配置文件

        * /etc/group
        
          字段详解(以":"为分隔符)

          组名 : 密码 : GID : 以此组为其附加组的用户列表

        * /etc/gshadow

***

### 用户管理

* 添加用户

      useradd [options] USERNAME
      option
      -u：UID
      -g：groupname 指定基本组
      -G：groupname,... 指定附加组
      -c："COMMENT"
      -d：指定家目录
      -s：指定SHELL路径
      -m -k：若家目录不存在，则自动创建
      -r：添加系统用户

* 删除用户

      userdel [options] USERNAME
      option
      -r：同时删除用户的家目录

* 查看用户的帐号属性信息

      id [options] USERNAME
      option
      -u：查看UID
      -g：查看GID
      -G: 查看所有的GID
      -n：查看组名
                                                                                          
      finger USERNAME


* 修改用户帐号属性

      usermod [options] USERNAME
      -u：UID
      -g：GID
      -a -g GID：不使用-a选项，会覆盖此前的附加组
      -d -m：指定新的家目录，并把之前家目录的文件拷贝到新的家目录中
      -c：
      -s：指定SHELL路径
      -L：锁定帐号
      -U：解锁帐号

* 密码管理

      passwd [USERNAME]
      --stdin：标准输入
      -d：删除用户密码

* 检查用户帐号完整性

      pwck

***

### 组管理

* 创建用户组：

      groupadd [option] GROUPNAME
      -g：GID
      -r：添加为系统组                                                                                                                                                                                

* 修改组的相关属性

      groupmod [option] GROUPNAME
      -g：GID
      -n：GRPNAME

* 删除组

      groupdel GROUPNAME                                                                                                                                                                                            

* 更改组密码

      gpasswd GROUPNAME

***

### 权限管理

* 改变文件属主

      chown USERNAME file,...
      -R：修改目录及其内部文件的属主
      --reference=/path/to/somefile file,...  指定属主与该文件相同
      chown USERNAME:GROUPNAME file 
      chown USERNAME.GROUPNAME file

* 改变属组

* 修改文件的权限

      chmod MODE file,...
      -R：
      --reference=/path/to/somefile
      修改单个用户的权限：u,g,o,a
      chmod 用户类别+|-MODE file,...
***
