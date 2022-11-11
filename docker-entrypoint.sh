#!/bin/sh

#python manage.py collectstatic --noinput -v0
python manage.py migrate

python manage.py runserver 9090
