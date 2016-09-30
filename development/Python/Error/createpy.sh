#!/bin/bash
#
#Written by: CC

FILE=$1

if [ -z $FILE ];then
	echo "Usage:$0 ,file name"
	echo "for example: sh $0 test.py"
	exit 1
fi

touch $FILE
echo "#!/usr/bin/env python" >> $FILE
echo "# -*- coding: utf-8 -*-" >> $FILE
echo "#@author: CC" >> $FILE
vim $FILE
