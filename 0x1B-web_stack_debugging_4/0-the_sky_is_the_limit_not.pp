# This make traffic go brr brr

# Increase the ULTIMate thingy
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart Nginx restart restart
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
