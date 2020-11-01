# django-celery
Background tasks with django, celery and redis.
 
## Requirements
Execute following commands:
```
sudo apt update
sudo apt-get install postgresql
sudo apt-get install python-psycopg2
sudo apt-get install libpq-dev
```
## Execute project local:

#### create virtual enviroment (execute these commands):
```
virtualenv 'name_enviroment'
source 'name_enviroment'/bin/activate
pip3 install -r requirements.txt
```
### executing the project:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
### Don't forget 
- create an celery broker and add it to settings.py
- add EMAIL_HOST to settings.py
- add the bd settings

## Execute project with nginx-gunicorn

### Installing ngninx
```
sudo apt install nginx
```
#### two step, set up firewall
```
sudo ufw app list
sudo ufw allow 'Nginx HTTP'
```
#### check firewall
```
sudo ufw status
```
#### check server web
```
systemctl status nginx
```
enter the localhost to verify. (http://localhost/)

#### other commands
```
sudo systemctl stop nginx
sudo systemctl start nginx
sudo systemctl restart nginx 
sudo systemctl reload nginx
sudo systemctl disable nginx
sudo systemctl enable nginx
```

### Check that gunicorn works
```
gunicorn --bind 0.0.0.0:8000 myproject.wsgi
```
check localhost:8000

## create socket and services files
The Gunicorn socket will be created on startup and will listen for connections. When a connection is established, systemd will automatically start the Gunicorn process to handle the connection.

1. create the file socket systemd for gunicorn
```
sudo nano /etc/systemd/system/gunicorn.socket
```
with these content:
```
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```
save and close the file.
2. create the file service systemd for gunicorn

```
sudo nano /etc/systemd/system/gunicorn.service
```
copy and paste the following:
```
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target
```
Now, we will open the [Service] section. We will specify the user and the group with which we want the process to run. We will grant ownership of the process to our normal user account, as it has ownership of all relevant files. We will grant group ownership to the www-data group so that Nginx can easily communicate with Gunicorn.

Next, we will map the working directory and specify the command that will be used to start the service. In this case, we will have to specify the full path to the Gunicorn executable, which is installed in our virtual environment. We will bind the process to the Unix socket we created in the / run directory so that the process can communicate with Nginx. We log all the data to standard output so that the journald process can collect the Gunicorn logs. We can also specify any optional Gunicorn settings here. For example, we specify 3 worker processes in this case:

```
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=william
Group=www-data
WorkingDirectory=/home/william/project/django-celery
ExecStart=/home/william/project/django-celery/env_celery/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          django_celery.wsgi:application
```
Lastly, we will add an [Install] section. This will tell systemd what to bind this service to if we enable it to load on startup. We want this service to start when the normal multi-user system is up and running:
```
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=william
Group=www-data
WorkingDirectory=/home/william/project/django-celery
ExecStart=/home/william/project/django-celery/env_celery/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \

[Install]
WantedBy=multi-user.target
```
save and close the file.
Now we can start and enable the Gunicorn socket. This will create the socket file in /run/gunicorn.sock now and on startup.
```
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
```
check the status of service:
```
sudo systemctl status gunicorn.socket
```
To test the socket triggering mechanism, we can send a connection to the socket via curl by typing the following:
```
curl --unix-socket /run/gunicorn.sock localhost
```
To restart the service of gunicorn if the file [/etc/systemd/systemd/system/gunicorn.service] has been changed, typing the following:
```
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
```
