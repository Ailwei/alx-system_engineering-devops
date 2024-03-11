# 0x1A. Application server

## Description
This project involves setting up an application server to complement the existing web server infrastructure, which currently serves web pages via Nginx. The application server will be integrated with Nginx to serve dynamic content, specifically the Airbnb clone project.

## Background Context
Your web infrastructure is already serving web pages via Nginx that you installed in your first web stack project. While a web server can also serve dynamic content, this task is usually given to an application server. In this project, you will add this piece to your infrastructure, plug it into your Nginx, and make it serve your Airbnb clone project.

## Resources
Read or watch:
- [Application server vs web server](https://www.digitalocean.com/community/tutorials/apache-vs-nginx-practical-considerations)
- [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04)
- [Running Gunicorn](https://docs.gunicorn.org/en/stable/run.html)
- [Be careful with the way Flask manages slash in route - strict_slashes](http://flask.pocoo.org/docs/1.0/api/#flask.Flask)
- [Upstart documentation](http://upstart.ubuntu.com/cookbook/)

## Requirements
### General
- A README.md file, at the root of the folder of the project, is mandatory
- Everything Python-related must be done using python3
- All config files must have comments

### Bash Scripts
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script is doing

