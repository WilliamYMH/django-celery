# django-celery
Background tasks with django, celery and redis.
 
## Requirements
Execute following commands:
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
