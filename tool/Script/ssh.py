#!/usr/bin/env python3
#-*- coding:utf-8 -*-

"""

使用ssh连接服务器并执行命令

"""

import paramiko
import time
import threading


def ssh_connect():
    try:
        # key = paramiko.RSAKey(data=base64.decodestring('AAA...'))
        client = paramiko.SSHClient()
        # client.get_host_keys().add('172.16.0.104', 'ssh-rsa', key)
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect('172.16.0.104', username='root', password='gbLEGlEY')
        stdin, stdout, stderr = client.exec_command('ls')
        out = stdout.readlines()
        print('\tOK\n')
        client.close()
    except:
        print('\tError\n')
        print(time.localtime())


ssh_connect()
