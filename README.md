Start, Stop and Restart Nginx using systemctl

SystemD is a system and service manager for the latest Ubuntu 18.04 /16.04 , CentOS 7 /8 , and Debian 10 /9 releases.

Whenever you make changes to the Nginx configuration, you need to restart or reload the webserver processes. Execute the following command to restart the Nginx service:

sudo systemctl restart nginx

When adding or editing server blocks, prefer reloading over restarting. Restart the service only when making significant modifications like changing ports or interfaces. On reload, Nginx loads the new configuration, starts new worker processes with the new configuration, and gracefully shuts down old worker processes.

Run the command below to reload the Nginx service:

sudo systemctl restart nginx

server setup /etc/nginx/sites-available/systemkonstruktion

Prometheus
=========

/etc/prometheus/prometheus.yml
/etc/systemd/system/prometheus.service

systemctl status prometheus

sudo systemctl daemon-reload
sudo systemctl start prometheus
sudo systemctl enable prometheus

