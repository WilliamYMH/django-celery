# django-celery
Background tasks with django, celery and redis.
 
## Requirements
Execute following commands:
- sudo apt update
- sudo apt-get install postgresql
- sudo apt-get install python-psycopg2
- sudo apt-get install libpq-dev

## Execute project:

#### create virtual enviroment (execute these commands):
- virtualenv 'name_enviroment'
- source 'name_enviroment'/bin/activate
 - pip3 install -r requirements.txt

### executing the project:
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

### Don't forget 
- create an celery broker and add it to settings.py
- add EMAIL_HOST to settings.py
- add the bd settings

## Setting up nginx with gunicorn

#### first, install nginx
-sudo apt install nginx

#### two step, set up firewall
- sudo ufw app list
- sudo ufw allow 'Nginx HTTP'

#### check firewall
- sudo ufw status
#### check server web
- systemctl status nginx
- enter the localhost to verify. (http://localhost/)
#### other commands
- sudo systemctl stop nginx
- sudo systemctl start nginx
- sudo systemctl restart nginx 
- sudo systemctl reload nginx
- sudo systemctl disable nginx
- sudo systemctl enable nginx
