#!/usr/bin/pup

# File: 1-install_a_package.pp

package { 'python3-pip':
  ensure => installed,
}
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => Package['python3-pip'],
}
package { 'werkeug':
  ensure   => '2.0.1',
  provider => 'pip',
  require  => Package['python3-pip'],
}
