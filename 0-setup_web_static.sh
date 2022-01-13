#!/usr/bin/env bash
#script that configures NGINX Folders and files
Placeholder="
  <head>
  </head>
  <body>
    Dummy Text
  </body>"

SED ="\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "$Placeholder" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i "35i $SED" /etc/nginx/sites-available/default
sudo service nginx restart
