# File: 2-puppet_custom_http_response_header.pp

# Install Nginx
class {'nginx': }

# Define custom HTTP response header
file { '/etc/nginx/conf.d/custom_headers.conf':
  ensure  => present,
  content => "add_header X-Served-By $hostname;\n",
  require => Class['nginx'],
  notify  => Service['nginx'],
}

# Restart Nginx to apply changes
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/conf.d/custom_headers.conf'],
}
