# Ensure holberton user exists and adjust open files limit

user { 'holberton':
  ensure => present,
}

# Adjusting open files limit for the holberton user
exec { 'increase-holberton-open-files-limit':
  command => 'echo "holberton hard nofile 10000" >> /etc/security/limits.conf && echo "holberton soft nofile 10000" >> /etc/security/limits.conf',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  unless  => 'grep -q "^holberton.*nofile.*10000" /etc/security/limits.conf',
}
