#!/usr/bin/env python
#-*- coding: utf-8 -*-

import logging
import logging.handlers
from cloghandler import ConcurrentRotatingFileHandler
import time
from random import choice
logger = logging.getLogger()
#handler = logging.handlers.RotatingFileHandler("logs/output.log","a",1024*1024*100,50)
handler = ConcurrentRotatingFileHandler("logs/output.log", "a", 1024*1024*100, 50)
formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

ip_array = ['172.16.0.111','192.168.2.9','10.8.0.3','172.15.3.22']
protocol_array = ['tcp','http','udp','icmp']
method_arry = ['PUT','GET','POST']
request_array = ['/','/hello/test','/happy/go','/sos/test']
header_arry = ['NULL','main:default:WAP:LABEL_CX-G_NORMAL_IP',\
                'apikey=7f8c4da3ce9849ffb2134f075201c45a&language=zh-CN&details=true',\
                'tcpmux: peer(218.8.127.165:9800) has 40 connections',\
                'iid=9529137899&device_id=35501623937&ac=4g&channel=store_aliyunos&aid=32&app_name=video_article&version_code=588&version_name=5.8.8&device_platform=android&user_version=1.1.8&ab_version=126489%2C125853%2C124728&ab_feature=z1&ssmix=a&device_type=Bird+D10&device_brand=BIRD&language=zh&os_api=22&os_version=5.1&uuid=862807030595172&openudid=32f5f18b092ba71e&manifest_version_code=118&resolution=720*1280&dpi=320&update_version_code=5881&_rticket=1496198125276']

while 1:
    num = choice(range(1,20000))
    for i in range(num):
        message = choice(ip_array) + ' ' + choice(protocol_array) + ' ' +\
        choice(method_arry) + ' ' + choice(request_array) + ' ' + choice(header_arry)
        logger.info(message)
    time.sleep(1)

