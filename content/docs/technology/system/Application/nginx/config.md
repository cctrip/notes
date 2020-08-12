---
bookCollapseSection: false
weight: 2
title: "配置"
---

# 配置

```nginx
user  www-data;
worker_processes auto;
worker_rlimit_nofile 650000;
pid /run/nginx.pid;

events {
    worker_connections 76800;
    # multi_accept on;
}

http {
	sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    #keepalive_timeout 1000;
        keepalive_timeout  120s 120s;
        keepalive_requests 1500;
    types_hash_max_size 2048;
    server_tokens off;
    #define request limit zone
        limit_req_zone $limit zone=req_limit:1024m rate=30r/s ;
        limit_req_zone $limit zone=auth_limit:1024m rate=10r/s ;
        limit_req_status 466;
        #limit_req_zone $binary_remote_addr zone=testreq:800m rate=1r/s;
        #define connection limit zone per ip
        limit_conn_zone  $limit zone=conn_limit:100m;
        
         # Gzip Settings
    ##
      gzip  on;
      gzip_http_version 1.0;
      gzip_comp_level 2;
      gzip_min_length 1100;
      gzip_buffers     4 8k;
      gzip_proxied any;
      gzip_types
        # text/html is always compressed by HttpGzipModule
        text/css
        text/javascript
        text/xml
        text/plain
        text/x-component
        application/javascript
        application/x-javascript
        application/json
        application/xml
        application/rss+xml
        font/truetype
        font/opentype
        application/vnd.ms-fontobject
        image/svg+xml
            image/jpeg
            image/gif
            image/png;

      #gzip_static on;

      gzip_proxied        expired no-cache no-store private auth;
      gzip_disable        "MSIE [1-6]\.";
      gzip_vary           on;
      
      
       # proxy config
         client_max_body_size 10m;
         client_body_buffer_size 128k;
         client_header_buffer_size 10k;
         proxy_connect_timeout 90;
         proxy_send_timeout 90;
         proxy_read_timeout 90;
         proxy_buffer_size 4k;
         proxy_buffers 4 32k;
         proxy_busy_buffers_size 64k;
         proxy_temp_file_write_size 64k;
         
         
         server {
         proxy_http_version 1.1;
        proxy_set_header Connection "";
         }
         
         }
```





```markdown
# 传输优化
# sendfile on;
一个正常的文件发送过程
1. malloc(3): 分配用于存储对象数据的本地缓冲区
2. read(2): 检索对象并将其复制到本地缓冲区
3. write(2): 将对象从本地缓冲区复制到套接字缓冲区

打开sendfile,该调用将一个对象检索到文件高速缓存，并将指针（不复制整个对象）直接传递给套接字描述符


# tcp_nodelay on;

为了避免网络拥塞，TCP协议栈通过Nagle算法实现了一种机制，该机制可以等待数据长达0.2秒，因此不会发送太小的数据包。(Nagle 算法原理是：在发出去的数据还未被确认之前，新生成的小数据先存起来，凑满一个 MSS 或者等到收到确认后再发送)
tcp_nodelay在HTTP keepalive状态中使用。

# tcp_nopush on;
与nodelay相反，它优化了一次发送的数据量，而不是优化延迟。一把在高延迟的网络中使用，增加一次发送的数据量。只有在启用了 sendfile 之后才生效。


# keepalive_timeout  120s 120s;
用于客户端不发送数据后保持连接的超时时间，第二个选项为header Keep-Alive: timeout=time的时间


# 数据压缩
gzip  on;
gzip_http_version 1.0;
gzip_comp_level 2;
gzip_min_length 1100;
gzip_buffers     4 8k;
gzip_types
  text/css
  text/javascript
  text/xml
  text/plain
  text/x-component
  application/javascript
  application/x-javascript
  application/json
  application/xml
  application/rss+xml
  font/truetype
  font/opentype
  application/vnd.ms-fontobject
  image/svg+xml
  image/jpeg
  image/gif
  image/png;
gzip_proxied        expired no-cache no-store private auth;
gzip_disable        "MSIE [1-6]\.";
gzip_vary           on;


# 代理优化
client_max_body_size 10m;
client_body_buffer_size 128k;
client_header_buffer_size 10k;
proxy_connect_timeout 90;
proxy_send_timeout 90;
proxy_read_timeout 90;
proxy_buffer_size 4k;
proxy_buffers 4 32k;
proxy_busy_buffers_size 64k;
proxy_temp_file_write_size 64k;


# buffer_size



```

