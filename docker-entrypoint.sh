#!/bin/sh

python manage.py migrate --noinput
python manage.py initadmin
python manage.py runserver 0.0.0.0:9090
