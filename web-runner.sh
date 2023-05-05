#!/bin/bash

python manage.py makemigrations.py --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn toursite.wsgi:application --bind 0.0.0.0:8000
