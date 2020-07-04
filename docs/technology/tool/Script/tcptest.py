#!/usr/bin/env python

"""

根据文本中的IP和端口进行可达性测试

"""

import socket
import sys

NORMAL = 0
ERROR = 1


def tcptest(ip, port):
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (str(ip), int(port))
    cs.settimeout(0.1)
    status = cs.connect_ex((address))
    # this status is returnback from tcpserver
    if status != NORMAL:
        return str(ip) + '------' + str(NORMAL)
    else:
        return str(ip) + '------' + str(NORMAL)

with open('ip.txt', 'r') as f:
    with open('ip.log', 'w') as g:
        for line in f.readlines():
            Ip, Port = line.split(',')
            result = tcptest(Ip, Port)
            g.write(result + '\n')
