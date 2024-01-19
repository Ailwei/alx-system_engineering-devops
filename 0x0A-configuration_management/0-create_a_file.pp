# A puppet manifest that creates a file school in /tmp.
# The file (School) has permissions 0744, belonging to the user and group www-data.

file { '/tmp/school':
  ensure  => present,         # Ensure that the file exists
  mode    => '0744',          # Set the permissions to 0744
  owner   => 'www-data',      # Set the owner to www-data
  group   => 'www-data',      # Set the group to www-data
  content => 'I love Puppet', # Set the content of the file
}
