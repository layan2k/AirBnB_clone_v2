# automates the task of creating a custom HTTP header response, but with Puppet

exec {'server-setup':
  provider => shell,
  $Placeholder = "
  <head>
  </head>
  <body>
    Dummy Text
  </body>",
  $SED = "\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"
  command  => 'sudo apt-get -y update && sudo apt-get -y upgrade && sudo apt-get -y install nginx && sudo mkdir -p /data/web_static/releases/test /data/web_static/shared && echo "$Placeholder" | sudo tee /data/web_static/releases/test/index.html && sudo chown -hR ubuntu:ubuntu /data/ && sudo sed -i "35i $SED" /etc/nginx/sites-available/default && sudo service nginx restart  ',
}
