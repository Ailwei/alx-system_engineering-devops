# 2-puppet_custom_http_response_header

# Install Nginx
class { 'nginx':
  manage_repo => true,
}

# Define Nginx vhost configuration with custom HTTP header
nginx::resource::vhost { 'default':
  listen_port => 80,
  proxy       => 'http://127.0.0.1:8080',
  server_name => '_',
  header      => ['X-Served-By $hostname'],
}

# Notify Nginx service to restart when the configuration changes
notify { 'Reload Nginx':
  subscribe => Nginx::Resource::Vhost['default'],
  exec      => '/usr/sbin/service nginx reload',
}
