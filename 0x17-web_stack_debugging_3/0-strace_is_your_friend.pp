# Fix type
exec  { 'replace':
    command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
    provider => '/bin'
}
