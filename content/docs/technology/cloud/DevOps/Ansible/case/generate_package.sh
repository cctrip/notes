#!/bin/bash

PRODUCT=$1
PROJECT=$2
DEST_PACKAGE_DIR=/cache1/ansible/test/packages/${PRODUCT}
CONF_DIR=${DEST_PACKAGE_DIR}/conf
SRC_PACKAGE_DIR=/update/${PRODUCT}

cd ${SRC_PACKAGE_DIR}
for pro in ${PROJECT[@]};do
    mkdir ${pro}
    unzip ${pro}.war -d ${pro}
    cp -a ${CONF_DIR}/${pro}/* ${SRC_PACKAGE_DIR}/${pro}/WEB-INF/classes/
    tar -zcf ${pro}.tar.gz ${pro}
    mv ${pro}.tar.gz ${DEST_PACKAGE_DIR}
    rm ${pro} -rf
done
