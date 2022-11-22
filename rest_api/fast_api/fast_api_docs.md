# Uvicorn

## Introduction
Uvicorn is an ASGI web server implementation for Python.
ASGI (Asynchronous Server Gateway Interface) is a spiritual successor to WSGI, 
intended to provide a standard interface between async-capable Python web servers, frameworks, and applications.

Where WSGI provided a standard for synchronous Python apps, ASGI provides one for both asynchronous and synchronous apps, 
with a WSGI backwards-compatibility implementation and multiple servers and application frameworks.

## Commands

### Start
``` shell
# The 'reload' flag allows to restart the service when a code update occurs
uvicorn <filename>:<fast_api_object> --reload

# Example
uvicorn first_api:service --reload
```