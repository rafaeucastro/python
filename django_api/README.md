# DJANGO FRAMEWORK

##### API in python using JDango

#### Some useful commands:
- `uv add django` - install the framework
- `django-admin startproject project-name` - start a new project
- `python manage.py startapp app-name` - create a new app / module
- `python manage.py runserver` - run the server
- `python manage.py makemigrations` - generate migration code
- `python manage.py migrate` - apply the migration code previously generated in the database
- `python manage.py createsuperuser` - create a new admin user for the control panel

#### Run with docker:
- `docker build -t djangoapi .` - build the image
- `docker run -d --name djangoapi -p 8000:8000 djangoapi`

#### Run services with docker-compose:
- `docker compose up -d --build`   