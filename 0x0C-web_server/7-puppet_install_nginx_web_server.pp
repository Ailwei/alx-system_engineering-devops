# Puppet manifest to install Nginx and configure it

# Install Nginx package
package { 'nginx':
  ensure => 'present',
}

# Update package repositories
exec { 'apt-update':
  command => 'sudo apt-get update',
  path    => '/usr/bin',
  require => Package['nginx'],
}

# Install Nginx
exec { 'install-nginx':
  command  => 'sudo apt-get -y install nginx',
  path     => '/usr/bin',
  require  => Exec['apt-update'],
  creates  => '/etc/nginx',
}

# Create Hello World index.html
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Exec['install-nginx'],
}

# Configure Nginx for redirect
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Exec['install-nginx'],
  notify  => Exec['nginx-restart'],
}

# Enable the redirect
nginx::resource::location { '/redirect_me':
  ensure   => present,
  location => '^/redirect_me',
  target   => 'https://www.youtube.com/',
  status   => 'permanent',
  require  => File['/etc/nginx/sites-available/default'],
  notify   => Exec['nginx-restart'],
}

# Restart Nginx service
exec { 'nginx-restart':
  command => 'sudo service nginx restart',
  path    => '/usr/bin',
  require => [Exec['install-nginx'], File['/etc/nginx/sites-available/default']],
}
