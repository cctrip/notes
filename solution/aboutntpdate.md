# 时间同步相关问题

#### ntpdate:no server suitable for synchronization found

##### Question：

　　在使用ntpdate同步时间时，出现了no server suitable for synchronization found的报错。

　　通过ntpdate -d s2m.time.edu.cn 使用debug模式没有出现异常。

##### Answer：

解决办法是，使用ntpdate -ubv s2m.time.edu.cn，可以正常同步了。

主要是-u选项的作用

	-u：Direct ntpdate to use an unprivileged port for outgoing packets. This is most useful when behind a firewall that blocks incoming traffic to privileged ports, and you want to synchronize with hosts beyond the firewall. Note that the -d option always uses unprivileged ports.

***

