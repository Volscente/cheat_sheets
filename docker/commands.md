---
title: "Commands"
tags: "Cheat Sheet"
---

# General

``` bash
docker version

docker info
```

<br>


# Docker Image

## List
``` bash
docker image ls
```

## Remove
``` bash
docker image rm <image_id/image_name>
docker image rm alpine ubuntu
```
## Pull
``` bash
docker image pull <image_name:image_tag>
docker image pull alpine:1.21.6
```

## Monitoring
``` bash
docker history <image_name>
docker image inspect <image_name>
```

## Tagging
``` bash
# source_image[:tag] target_image[:tag]
docker image tag nginx volscente/nginx
```

## Push
``` bash
# Login into Docker Hub
docker login

# Push the image
docker image push target_image[:tag]
```

<br>


# Docker Container

## Run
``` bash
docker container run -p 80:80 -d --name nginx_container nginx

# --rm delete container after exit
docker container run -it --rm <image_name> bash
```

## List
``` bash
docker container ls
docker container ls -a
```

## Start & Stop
``` bash
docker container stop [<container_id/container_name>]
docker container start [<container_id/container_name>]
```

## Remove
``` bash
docker container rm -f [<container_id/container_name>]
```

## Monitoring
``` bash
docker container logs <container_id/container_name>

docker container top <container_id/container_name>

docker container inspect <container_id/container_name>

docker container stats <container_id/container_name>
```

## Container Shell
``` bash
# Run a container with a bash shell open
docker container run -it --name <container_name> <image_name> bash

# Start a container with a bash shell open
docker container start -ai <container_name>

# Execute the bash command inside a running container
docker container exec -it <container_name> bash

# Execute a command in a one-shot container
docker container run -it --rm centos:7 curl -s search:9200
```

## Networking
``` bash
# Show port mapping
docker container port <container_id/container_name>

# Show container ip
docker container inspect --format '{{.NetworkSettings.IPAddress }}' <container_id/container_name>
```

<br>


# Docker Network

## List
``` bash
docker network ls
```

## Monitoring
``` bash
docker network inspect <network_id/network_name>
```
![image.png](https://boostnote.io/api/teams/TL5N63v1i/files/5da907762cb96a20b853b947c1b72072df6fa9366a5fa65f2fd819371158483e-image.png)
It shows the containers attached to that network and it's IP (IPAM)

## Create
``` bash
docker network create <network_name>

# Example on how to use it
docker container run -d --name <container_name> --network <network_name> <image>
```

## Connect & Disconnect
``` bash
docker network connect <network_id/network_name> <container_id/container_name>

docker network disconnect <network_id/network_name> <container_id/container_name>
```

## DNS
Docker uses container's names for DNS, which is more reliable thanIPs

``` bash
# --network-alias allows to specify a DNS alias
# Same alias can be assigned to multiple containers
docker container run -d --name elasticsearch1 --network app_net --network-alias es elasticsearch:2

docker container run -d --name elasticsearch2 --network app_net --network-alias es elasticsearch:2
```
