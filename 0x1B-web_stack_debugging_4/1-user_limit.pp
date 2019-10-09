# Fix file extension
exec { 'fix-file':
  path     => '/usr/bin:/usr/sbin:/bin',
  provider => shell,
  command  => "sed -i 's/nofile .*/nofile 50000/g' /etc/security/limits.conf",
}
