# 0x0C. Web Server

## DevOps | SysAdmin
**By: Sylvain Kalache**  
*Weight: 1*  
*Project starts: Jan 22, 2024 6:00 AM*  
*Project ends: Jan 24, 2024 6:00 AM*  
*Checker released: Jan 22, 2024 6:00 PM*  
*Auto review deadline: Jan 24, 2024 6:00 AM*

## Concepts
### What is a Child Process?
In this project, understanding the concept of a child process is crucial.

## Background Context
In this project, tasks will be graded on two aspects:
1. Is your web-01 server configured according to requirements?
2. Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine without any human intervention?

Example Bash script in the answer file:
```bash
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default

# Web Server Configuration Project

## Introduction
This project aims to configure a web server (web-01) according to specified requirements. The checker will execute your scripts as the root user, eliminating the need for the sudo command.

> "A good Software Engineer is a lazy Software Engineer."

## Tips for Testing
To test your Bash script, reproduce the checker environment:
1. Start a Ubuntu 16.04 sandbox.
2. Run your script on it.
3. Observe its behavior.

## Resources
Read or watch:
- [How the web works](#)
- [Nginx](#)
- [How to Configure Nginx](#)
- [Child process concept page](#)
- [Root and subdomain](#)
- [HTTP requests](#)
- [HTTP redirection](#)
- [Not found HTTP response code](#)
- [Logs files on Linux](#)

For reference:
- [RFC 7231 (HTTP/1.1)](https://tools.ietf.org/html/rfc7231)
- [RFC 7540 (HTTP/2)](https://tools.ietf.org/html/rfc7540)

Man or help:
- `scp`
- `curl`

## Learning Objectives
By the end of this project, you should be able to explain:
- What is the main role of a web server?
- What is a child process?
- Why web servers usually have a parent process and child processes?
- What are the main HTTP requests?
- DNS
  - What DNS stands for
  - What is DNS's main role
  - DNS Record Types: A, CNAME, TXT, MX

## Copyright - Plagiarism
- Come up with solutions for the tasks yourself to meet learning objectives.
- No copying and pasting someone else’s work.
- No publishing any content of this project.
- Strictly forbid plagiarism; it will result in removal from the program.

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- Interpreted on Ubuntu 16.04 LTS
- Files end with a new line
- `README.md` is mandatory
- All Bash script files must be executable
- Bash scripts must pass Shellcheck (version 0.3.7) without any error
- First line of all Bash scripts: `#!/usr/bin/env bash`
- Second line of all Bash scripts should be a comment explaining the script's purpose
- Cannot use `systemctl` for restarting a process
