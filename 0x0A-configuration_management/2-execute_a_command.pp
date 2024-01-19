# File: 2-execute_a_command.pp

exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin:/bin', # Adjust the path as needed
  onlyif  => 'pgrep -f killmenow', # Ensure the process is running before attempting to kill
}
