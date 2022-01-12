# automates the task of creating a custom HTTP header response, but with Puppet

exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install Nginx'],
}

exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['Make Release Folder'],
}

exec { 'Make Release Folder':
  provider    => shell,
  command     => 'sudo mkdir -p /data/web_static/releases',
  before      => Exec['Make Shared Folder'],
}

exec { 'Make Shared Folder':
  provider    => shell,
  command     => 'sudo mkdir -p /data/web_static/shared',
  before      => Exec['Test Folder'],
}

exec { 'Test Folder':
  provider    => shell,
  command     => 'sudo mkdir -p /data/web_static/releases/test',
  before      => Exec['touch_index'],
}

exec { 'touch_index':
  provider    => shell,
  command     => 'sudo touch /data/web_static/releases/test/index.html',
  before      => Exec['write_index'],
}

exec { 'write_index':
  provider    => shell,
  command     => 'sudo echo "Dummy Text" > /data/web_static/releases/test/index.html',
  before      => Exec['symbolic_link'],
}
exec { 'symbolic_link':
  provider    => shell,
  command     => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  before      => Exec['permissions'],
}
exec { 'permissions':
  provider    => shell,
  command     => 'sudo chown -R ubuntu:ubuntu /data/',
  before      => Exec['nginx_config'],
}
exec { 'nginx_config':
  provider    => shell,
  command     => 'sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default',
  before      => Exec['restart Nginx'],
}

exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
