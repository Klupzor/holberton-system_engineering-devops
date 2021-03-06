# puppet file to config server
exec { 'update':
  command  => 'sudo apt-get update',
  provider => shell,
}
-> package{'nginx':
  ensure => present,
}
-> file_line {'insert_line':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "	location / {
  	add_header X-Served-By ${hostname};",
  match  => '^\tlocation / {',
}
-> exec { 'restart service nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
}
