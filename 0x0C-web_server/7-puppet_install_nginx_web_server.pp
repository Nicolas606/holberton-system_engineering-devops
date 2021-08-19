# Installs nginx web server using puppet
package {'Install nginx':
  ensure => installed,
  name   => 'nginx',
}

file { '/var/www/html/index.html':
  content => 'Holberton School for the win!',
}
