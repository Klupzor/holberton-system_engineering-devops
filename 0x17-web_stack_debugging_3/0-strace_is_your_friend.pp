exec { 'fix-file':
  path     => '/usr/bin:/usr/sbin:/bin',
  provider => shell,
  command  => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g'\
/var/www/html/wp-settings.php",
}
