---
bookCollapseSection: true
weight: 2
title: "Ansible"
---

# Ansible

### 安装

* 安装ansible

      pip install ansible

* 测试
  
      echo "127.0.0.1" > ~/ansible_hosts
    
      export ANSIBLE_INVENTORY=~/ansible_hosts
    
      ansible all -m ping --ask-pass

### Inventory

* 主机和组

    ansible_hosts 文件

      [group1]
      host1 
      host2

      [group2]
      host3
      host4

      ssh选项
      ansible_port=5555(默认22)
      ansible_host=172.16.0.101 
      ansible_user=root(默认root)
      ansible_connection=ssh(默认ssh)
      ansible_ssh_pass=

      host变量
      http_port=80 
      maxRequestsPerChild=808

      group变量
      [group1:vars]
      ansible_port=33

      group包含group
      [group3:children]
      group1
      group2

***

### 命令行

    ansible <server_name> -m <module_name> -a <arguments>

***

### 配置文件

略

### Playbook

Playbook是Ansible的配置，部署和编排语言，他们可以描述您希望远程系统执行的策略，或一般IT流程中的一组步骤。


一个playbook案例

    ---
    - hosts: webservers
      vars:
        http_port: 80
        max_clients: 200
      remote_user: root
      tasks:
      - name: ensure apache is at the latest version
        yum: name=httpd state=latest
      - name: write the apache config file
        template: src=/srv/httpd.j2 dest=/etc/httpd.conf
        notify:
        - restart apache
      - name: ensure apache is running (and enable it at boot)
        service: name=httpd state=started enabled=yes
      handlers:
        - name: restart apache
          service: name=httpd state=restarted

***

### roles



***

### 案例

* [tomcat](case/tomcat-project.yml)

* [tengine](case/tengine.yml)

* [zookeeper](case/zookeeper.yml)

* [kafka](case/kafka.yml)