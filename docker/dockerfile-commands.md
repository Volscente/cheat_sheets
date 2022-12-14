---
title: "Dockerfile Commands"
tags: "Cheat Sheet"
---

# Commands
``` dockerfile
# The base image
FROM <image_name>[:tag]

# Environment Variables
ENV <env_variable_name> <value>

# Run commands
RUN <commands>

# Expose ports
PORT <list_of_ports>

# Change the current directory into the container
WORKDIR <path>

# Copy an element into the container
COPY <local_file> <path_into_container>

# Commands
CMD ["<command1>", "<command2>", "<...>"]
```

<br>

# Example
``` dockerfile
FROM debian:jessie

ENV NGINX_VERSION 1.11.1

# The reason to chain multiple commands into the same RUN is that each Dockerfile
# command (e.g., FROM, ENV, etc.) is a single image layer
# In this way, all the commands in the RUN will go in the same layer
RUN apt-get update \
    && apt-get install curl -y \
    && rm -rf /var/lib/apt/lists/*

# This does not mean that the ports 80 443 would be expose, that's what the
# -p on docker container run does
EXPOSE 80 443

# Change the working directory
WORKDIR /usr/share/nginx/html

# Copy a file 'index.html' into the container
COPY index.html index.html

CMD ["nginx", "-g", "daemon off;"]
```

<br>


# Build Image
``` bash
# Run inside the folder with the Dockerfile
docker image build -t [repository/]<image_name>[:tag] .

docker image build -t volscente/new_nginx:1.0.0 .
```
