# 0. Strace is your friend
exec  { 'replace':
    command  => 'sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
    provider => '/bin'
}
