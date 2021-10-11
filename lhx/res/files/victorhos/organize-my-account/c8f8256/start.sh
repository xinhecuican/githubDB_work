#!/bin/bash

python manage.py makemigrations
python manage.py migrate
python manage.py runserver ${DJANGO_BIND_ADDRESS}:${DJANGO_BIND_PORT}
