# execute pkill to kill killmenow
exec { 'pkill':
  command => 'pkill -9 -f killmenow',
  path    => ['/bin', '/usr/bin'],
}
