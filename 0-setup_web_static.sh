#!/usr/bin/env bash
#script that configures NGINX Folders and files
sudo apt-get -y update
sudo apt-get install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "Dummy Text" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
