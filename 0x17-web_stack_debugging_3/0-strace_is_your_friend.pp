# Fix file extension
exec { 'fix-file':
  path     => '/usr/bin:/usr/sbin:/bin',
  provider => shell,
  command  => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
}
