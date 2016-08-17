#!/bin/sh
#
# snortd         Start/Stop the snort IDS daemon.
#
# chkconfig: 2345 40 60
# description:  snort is a lightweight network intrusion detection tool that
#               currently detects more than 1100 host and network
#               vulnerabilities, portscans, backdoors, and more.
#
# June 10, 2000 -- Dave Wreski <dave@linuxsecurity.com>
#   - initial version
#
# July 08, 2000 Dave Wreski <dave@guardiandigital.com>
#   - added snort user/group
#   - support for 1.6.2
# July 31, 2000 Wim Vandersmissen <wim@bofh.st>
#   - added chroot support

# Source function library.
. /etc/rc.d/init.d/functions

# source the interface to listen on
. /etc/sysconfig/snort

# See how we were called.
case "$1" in
  start)
        echo -n "Starting snort: "
	if [ -f /var/lock/subsys/snort ];then
		status snort
	else
        	cd /var/log/snort
        	daemon /usr/local/snort/bin/snort -D $SNORT_OPTIONS \
                	-c /etc/snort/etc/snort.conf
        	touch /var/lock/subsys/snort
	fi
        # for NFQ mode
	/sbin/iptables -t raw -nL | grep "NFQUEUE" 2>&1 >/dev/null
	RETV=$?
	if [ $RETV != 0 ];then
		/sbin/iptables -t raw -A PREROUTING -p tcp -m multiport --dports 8080 -j NFQUEUE --queue-num 8
		#/sbin/iptables -t raw -A PREROUTING -p udp -j NFQUEUE --queue-num 8
	else
		exit $RETV	
	fi
        echo
        ;;
  stop)
        echo -n "Stopping snort: "
        # for NFQ mode
		/sbin/iptables -t raw -D PREROUTING -p tcp -m multiport --dports 8080 -j NFQUEUE --queue-num 8
		#/sbin/iptables -t raw -D PREROUTING -p udp -j NFQUEUE --queue-num 8
        killproc snort
        rm -f /var/lock/subsys/snort
        echo 
        ;;
  restart)
        $0 stop
        $0 start
        ;;
  status)
        status snort
        ;;
  *)
        echo "Usage: $0 {start|stop|restart|status}"
        exit 1
esac

exit 0
