# ELK安装

### 环境准备

* CentOS 7

* Java 8

***

### ELK安装

* 配置ELK的repo文件

      rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch

      #vim /etc/yum.repo.d/elk.repo
      [elasticsearch-6.x]
      name=Elasticsearch repository for 6.x packages
      baseurl=https://artifacts.elastic.co/packages/6.x/yum
      gpgcheck=1
      gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
      enabled=1
      autorefresh=1
      type=rpm-md

* ElasticSearch

      #install
      yum install elasticsearch
      /bin/systemctl daemon-reload
      /bin/systemctl enable elasticsearch.service
      systemctl start elasticsearch.service

      #Test
      curl http://localhost:9200/

* Kibana

      #install
      yum install kibana
      /bin/systemctl daemon-reload
      /bin/systemctl enable kibana.service

      #vim /etc/kibana/kibana.yml
      server.host: 0.0.0.0

* LogStash

      #install
      yum install logstash
      /bin/systemctl start logstash.service

* Filebeat

      #install
      yum -y install filebeat

***

### 配置

* 配置hosts

      #vim /etc/hosts
      192.168.19.26 elk.cctest.com

* 生成SSL证书

      cd /etc/pki/tls
      openssl req -subj '/CN=elk.cctest.com/' -x509 -days 3650 -batch -nodes -newkey rsa:2048 -keyout private/logstash-forwarder.key -out certs/logstash-forwarder.crt

* logstash配置

      #vim /etc/logstash/conf.d/02-beats-input.conf
      input {
        beats {
          port => 5044
          ssl => true
          ssl_certificate => "/etc/pki/tls/certs/logstash-forwarder.crt"
          ssl_key => "/etc/pki/tls/private/logstash-forwarder.key"
        }
      }

      #vim /etc/logstash/conf.d/10-log-filter.conf
      filter {
        grok {
          match => { "message" => "%{COMBINEDAPACHELOG}" }
        }
        geoip {
          source => "clientip"
        }
      }

      #vim /etc/logstash/conf.d/30-elasticsearch-output.conf
      output {
        elasticsearch {
          hosts => ["localhost:9200"]
        }
      }

      #重启logstash
      /bin/systemctl restart logstash.service

* filebeat配置

      #vim /etc/filebeat/filebeat.yml
      filebeat.prospectors:
      - type: log
      enabled: true
      paths:
        - /var/log/messages*

      filebeat.config.modules:
        path: ${path.config}/modules.d/*.yml
        reload.enabled: false

      setup.template.settings:
        index.number_of_shards: 3

      output.logstash:
        hosts: ["elk.cctest.com:5044"]
        ssl.certificate_authorities: ["/etc/pki/tls/certs/logstash-forwarder.crt"]

      #
      systemctl start filebeat


* 浏览器打开kibana

      http://localhost:5601/

    ![kibana-screen](kibana-screen.png)