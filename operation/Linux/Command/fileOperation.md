# 一切皆文件

* 列出文件列表

        ls [option] /PATH #不指定路径，默认为当前路径  
        option
          -l:长格式
            文件类型:
              -:普通文件
              d:目录文件
              b:块设备文件（block）
              c：字符设备文件（character）
              l：符号链接文件（symbolic link file）
              p：命令管道（pipe）
              s：套接字文件（socket）
            文件权限：9位，每三位一组(u-g-o),每一组：rwx（读、写、执行）
            文件硬链接的次数
            文件的属主(owner)
            文件的属组(group)
            文件的大小(size)，单位是字节
            时间戳(timestamp)：最近一次被修改的时间
              访问：access
              修改：modify，文件内容发生改变
              改变：change，metadata，元数据
            文件名
          -h:做单位转换，默认bit
          -a:显示以.开头的隐藏文件
            . 表示当前目录
            .. 表示父目录
          -d：显示目录自身属性
          -i：index node，inode
          -r：逆序显示文件
          -R：递归(recursive)显示 

* 进入目录

        cd /PATH
        cd ~USERNAME:进入指定用户的家目录
        cd -:在当前目录和前一次所在目录之间来回切换

* 显示文件类型

        type /PATH/FILENAME

* 显示当前路径

        pwd

* 目录管理

    * 创建空目录

           mkdir [option] /PATH
            option
              -p:若父目录不存在，则自动创建
              -v:列出过程详细信息
              -m:指定目录权限

    * 删除空目录

            rmdir /PATH

* 文件管理

    * 创建文件

            touch [option] /PATH
            option:若文件存在
              -a:修改访问时间
              -m:修改修改时间
              -c:修改改变时间

    * 查看文件状态

            stat /PATH

    * 删除文件
    
            rm [option] /PATH
            option
              -i:提示
              -f:强制删除，不提示
              -r:递归删除

    * 复制文件

            cp [option] SRC DEST
            option
              -r:递归
              -i:提示是否覆盖
              -p:保留属性
              -a:归档复制，保留所有属性

    * 移动文件

            mv SRC DEST

* 文本查看

    * 连接并显示

            cat [option] /PATH/FILENAME
            option
              -n:显示行号
              -E:显示行尾

    * 分屏显示

            more /PATH/FILENAME

            less /PATH/FILENAME

            head [option] /PATH/FILENAME
            option
              -n number:显示前n行

            tail [option] /PATH/FILENAME
            option
              -n number:显示后n行
              -f:查看文件尾部，不退出，等待显示后续追加至此文件的新内容

* 文本处理

    * 文本分割

            cut [option] /PATH/FILENAME
            option
              -d:指定分隔符，默认是空格
              -f number:指定要显示的字段

    * 文本排序

            sort [option] /PATH/FILENAME
            option
              -n:数值排序
              -r:降序 #默认为升序
              -t:字段分隔符
              -k:以哪个字段为关键字进行排序
              -u:排序后相同的行只显示一次

    * 文本去重
    
            uniq [option] /PATH/FILENAME
            option 
              -c:只显示文件中行重复的次数
              -d:只显示重复的行

    * 文本统计

            wc [option] /PATH/FILENAME
            option
              -l:统计行数
              -w:统计单词数
              -c:统计字符数
              -L:打印最长的行

    * 字符转换
        
            tr [option] SET1 [SET2]
            option
              -d:删除出现在字符集中的所有字符

