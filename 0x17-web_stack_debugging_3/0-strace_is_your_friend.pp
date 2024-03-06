# Puppet manifest to fix Apache 500 Internal Server Error

file { '/path/to/missing/file':
  ensure => file,
  owner  => 'apache',
  group  => 'apache',
  mode   => '0644',
  source => 'puppet:///modules/my_module/missing_file',
}
