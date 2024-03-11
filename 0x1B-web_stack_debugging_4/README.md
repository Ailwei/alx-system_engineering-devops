# 0x1B. Web stack debugging #4

## Description
This project focuses on debugging issues within a web stack environment.

## Requirements
### General
- All files will be interpreted on Ubuntu 14.04 LTS.
- All files should end with a new line.
- A `README.md` file at the root of the folder of the project is mandatory.
- Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors.
- Puppet manifests must run without error.
- Puppet manifests' first line must be a comment explaining what the Puppet manifest is about.
- Puppet manifest files must end with the extension `.pp`.
- Files will be checked with Puppet v3.4.

### Installation Steps
```bash
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
