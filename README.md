```
vim /etc/hosts
    127.0.0.1 example.com

vim proxy/example.conf
    proxy_set_header X-Forwarded-Host $host:$server_port;
    # proxy_set_header X-Forwarded-Host $http_host;
bash run.sh
curl example.com:8000
# {"url": "http://example.com/"}

vim proxy/example.conf
    # proxy_set_header X-Forwarded-Host $host:$server_port;
    proxy_set_header X-Forwarded-Host $http_host;
bash run.sh
curl example.com:8000
# {"url": "http://example.com:8000/"}
```
