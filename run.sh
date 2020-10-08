#!/bin/bash
THIS_FOLDER=$(cd "$(dirname "$BASH_SOURCE[0]")" >/dev/null 2>&1 && pwd)

podman pod rm example -f
podman pod create --name example -p 8000:80

podman run -d --pod example \
    -v $THIS_FOLDER/server:/root \
    docker.io/library/python \
    bash /root/run.sh

podman run -d --pod example \
    -v $THIS_FOLDER/proxy:/etc/nginx/conf.d \
    docker.io/library/nginx
