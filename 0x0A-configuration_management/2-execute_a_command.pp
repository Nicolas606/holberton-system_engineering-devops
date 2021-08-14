# create a manifest that kills a process named killmenow.

exec  { 'kill Poccess':
  command  => 'pkill killmenow',
  provider => 'shell'
}
