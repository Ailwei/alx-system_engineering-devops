# 0x0B. SSH DevOps Project

## Author
Sylvain Kalache

## Overview
This project involves setting up and configuring SSH on an Ubuntu server, emphasizing the use of RSA key pairs for secure authentication. The project is part of the learning objectives in the field of DevOps, covering topics related to SSH, networking, system administration, and security.

## Project Details
- Weight: 1
- Project Start: Jan 19, 2024 6:00 AM
- Project End: Jan 22, 2024 6:00 AM
- Checker Released: Jan 20, 2024 12:00 AM
- Auto Review Deadline: Jan 22, 2024 (at the project end)

## Background Context
You've been assigned an Ubuntu server located in a distant datacenter. Access to the server will be through SSH using an RSA key instead of a password. Server information, including IP and username, is available in the "my servers" section of the intranet.

Note: The server is configured with Ubuntu 20.04 LTS.

## Resources
- [What is a (physical) server - text](link-to-text-resource)
- [What is a (physical) server - video](link-to-video-resource)
- [SSH essentials](link-to-ssh-essentials)
- [SSH Config File](link-to-ssh-config-file)
- [Public Key Authentication for SSH](link-to-public-key-auth)
- [How Secure Shell Works](link-to-how-ssh-works)
- [SSH Crash Course](link-to-ssh-crash-course) (Long, but highly informative.)

## Reference Materials
- [Understanding the SSH Encryption and Connection Process](link-to-ssh-encryption)
- [Secure Shell Wiki](link-to-ssh-wiki)
- [IETF RFC 4251 (Description of the SSH Protocol)](link-to-ietf-rfc-4251)
- [Internet Engineering Task Force](link-to-ietf)
- [Request for Comments (RFC)](link-to-rfc)

## Man or Help Commands
- `ssh`
- `ssh-keygen`
- `env`

## Learning Objectives
By the end of this project, you should be able to explain:
1. What is a server
2. Where servers usually live
3. What is SSH
4. How to create an SSH RSA key pair
5. How to connect to a remote host using an SSH RSA key pair
6. The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash`

## Copyright - Plagiarism
- Do not copy and paste someone else’s work.
- No publishing of project content.
- Plagiarism results in removal from the program.

## Requirements
- Editors: vi, vim, emacs
- Interpreted on Ubuntu 20.04 LTS
- Files end with a new line
- Mandatory README.md file at the root
- Bash script files must be executable
- First line: `#!/usr/bin/env bash`
- Second line: Comment explaining the script's purpose
