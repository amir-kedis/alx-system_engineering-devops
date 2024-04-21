# Ensure flask v2.1.0 is installed
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
