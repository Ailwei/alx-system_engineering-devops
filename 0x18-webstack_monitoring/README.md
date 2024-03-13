# 0x18. Webstack monitoring

## Description
This project focuses on implementing web stack monitoring, which involves both application monitoring and server monitoring. The goal is to gather data about running software and ensure it behaves as expected, while also collecting data about virtual or physical servers to prevent overload issues.

## Concepts
- Monitoring
- Server

## Background Context
“You cannot fix or improve what you cannot measure” is a famous saying in the Tech industry. In the age of data-ism, monitoring how our Software systems are doing is an important thing. In this project, we will implement one of many tools to measure what is going on our servers.

Web stack monitoring can be broken down into 2 categories:
- Application monitoring: getting data about your running software and making sure it is behaving as expected
- Server monitoring: getting data about your virtual or physical server and making sure they are not overloaded (could be CPU, memory, disk, or network overload)

## Resources
Read or watch:
- [What is server monitoring](URL)
- [What is application monitoring](URL)
- [System monitoring by Google](URL)
- [Nginx logging and monitoring](URL)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
- Why monitoring is needed
- What are the 2 main areas of monitoring
- What are access logs for a web server (such as Nginx)
- What are error logs for a web server (such as Nginx)

## Requirements
- Allowed editors: vi, vim, emacs
- Interpreted on Ubuntu 16.04 LTS
- All files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7) without any error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what the script is doing