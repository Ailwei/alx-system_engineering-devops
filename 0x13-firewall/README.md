## 0x13. Firewall

### Description
In this project, we will be setting up a firewall on our servers to enhance security. The firewall will be configured to allow specific incoming traffic while blocking all other traffic.

### Concepts
For this project, it's important to understand:

- Web stack debugging

### Background Context
Without a firewall, servers are susceptible to various security threats. A firewall helps control incoming and outgoing traffic based on predetermined security rules.

### Resources
- [What is a firewall](https://en.wikipedia.org/wiki/Firewall_(computing))

### Tasks

#### Mandatory
- Configure UFW firewall on `web-01` to block all incoming traffic except for ports 22 (SSH), 443 (HTTPS), and 80 (HTTP).

#### Additional

### Author
By Sylvain Kalache, co-founder at Holberton School

### Timeline
- Project started: Feb 12, 2024 6:00 AM
- Project ends: Feb 13, 2024 6:00 AM
- Checker release: Feb 12, 2024 12:00 PM
- Auto-review deadline: Feb 13, 2024 6:00 AM

### Notes
- Telnet can be used to check if ports are open.
- Testing should be performed from outside the school network to bypass the network-based firewall filtering outgoing connections.

