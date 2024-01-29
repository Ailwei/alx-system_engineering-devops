# 0x0F. Load Balancer

## Backend Configuration

### Project Details

- **Domain:** DevOps, SysAdmin
- **Author:** Sylvain Kalache, co-founder at Holberton School
- **Weight:** 1
- **Start Date:** Jan 29, 2024 6:00 AM
- **End Date:** Jan 30, 2024 6:00 AM
- **Checker Release:** Jan 29, 2024 12:00 PM
- **Auto Review Deadline:** Jan 30, 2024 6:00 AM

### Concepts

This project focuses on the following concepts:

- Load balancer
- Web stack debugging

### Background Context

Two additional servers have been provided:

- `gc-[STUDENT_ID]-web-02-XXXXXXXXXX`
- `gc-[STUDENT_ID]-lb-01-XXXXXXXXXX`

The objective is to enhance the web stack for redundancy, enabling the infrastructure to handle more traffic by doubling the number of web servers. This ensures reliability, even if one web server fails.

### Resources

Read or watch:

- [Introduction to load-balancing and HAproxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
- [HTTP header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)
- [Debian/Ubuntu HAProxy packages](http://www.haproxy.org/download/2.0/doc/debpacking.html)

### Requirements

#### General

- **Allowed Editors:** vi, vim, emacs
- **Interpreted On:** Ubuntu 16.04 LTS
- **File Ending:** All files should end with a new line
- **Mandatory File:** README.md file at the root of the project folder
- **Bash Scripts:** All Bash script files must be executable
- **Shellcheck:** Bash scripts must pass Shellcheck (version 0.3.7) without any error
- **Shebang:** The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- **Comments:** The second line of all Bash scripts should be a comment explaining what is the script doing
