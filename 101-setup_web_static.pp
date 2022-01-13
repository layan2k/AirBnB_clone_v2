# automates the task of creating a custom HTTP header response, but with Puppet

exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['upgrade'],
}

exec {'upgrade':
  provider => shell,
  command  => 'sudo apt-get -y upgrade',
  before   => Exec['install Nginx'],
}

exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['Make Release Folder'],
}

exec { 'Make Release Folder':
  provider    => shell,
  command     => 'sudo mkdir -p /data/web_static/releases /data/web_static/shared',
  before      => Exec['write_index'],
}

exec { 'write_index':
  provider    => shell,
  environment => [Placeholder="
  <head>
  </head>
  <body>
    Dummy Text
  </body>"]
  command     => 'echo "$Placeholder" | sudo tee /data/web_static/releases/test/index.html',
  before      => Exec['symbolic_link'],
}

exec { 'symbolic_link':
  provider    => shell,
  command     => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  before      => Exec['permissions'],
}

exec { 'permissions':
  provider    => shell,
  command     => 'sudo chown -hR ubuntu:ubuntu /data/',
  before      => Exec['nginx_config'],
}

exec { 'nginx_config':
  provider    => shell,
  environment => [SED="\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"]
  command     => 'sudo sed -i "35i $SED" /etc/nginx/sites-available/default',
  before      => Exec['restart Nginx'],
}

exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
