#!/usr/bin/env bash
# sets up web server for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /var/www/html
sudo service nginx start

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test

sudo echo "Holberton School" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data

sudo cat > /etc/nginx/sites-available/default <<EOF
server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;
	server_name _;

	location /hbnb_static {
		alias /data/web_static/current;
	}
}
EOF

sudo service nginx reload
sudo service nginx restart
