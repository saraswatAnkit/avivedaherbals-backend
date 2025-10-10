#!/bin/bash
docker exec avivedaherbals-django python manage.py migrate --noinput
docker exec avivedaherbals-django python manage.py collectstatic --noinput
