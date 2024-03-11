# Fix for Nginx to handle high volume of requests
exec { 'fix--for-nginx':
  command     => 'sed -i "s/return 404;/return 200;/g" /etc/nginx/sites-available/default',
  path        => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  refreshonly => true,
}

# Restart Nginx service after applying fixes
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => Exec['fix--for-nginx'],
}
