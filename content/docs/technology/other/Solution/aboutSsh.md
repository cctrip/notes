# ssh连接相关问题

#### pam_tally2(sshd:auth): user root (0) has time limit [3s left] since last failure 日志

##### Question：

工作中，碰到某服务器在批量ssh登陆操作时，出现大量的无法连接的情况。

##### Thinking：
查看ssh日志(/var/log/secure)，
首先注意到的是，"Failed password for root from xxx.xxx.xxx.xxx port 51230 ssh2"错误，但发现密码并没有错误，并且只在批量操作时才会出现，故初步判断为连接数问题。

查看ssh连接数限制

	/usr/sbin/sshd -T | grep -i max

调整参数，更改配置文件/etc/sshd/sshd_config
	
	maxsessions 1000

重启服务后，依然没有效果。

再次查看日志，发现在做批量操作时，有大量的"pam_tally2(sshd:auth): user root (0) has time limit [3s left] since last failure"日志。 

应该是pam模块做了相应的限制

查看配置文件 /etc/pam.d/sshd 文件

	auth       required    pam_tally2.so   deny=10  lock_time=3 unlock_time=30 even_deny_root root_unlock_time=30

#### Answer：

更改配置文件：

	#auth       required    pam_tally2.so   deny=10  lock_time=3 unlock_time=30 even_deny_root root_unlock_time=30

***

