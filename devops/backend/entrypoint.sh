#!/bin/sh

echo 'Waiting for PostgreSQL...'

while ! nc -z $DB_HOST $DB_PORT; do
    echo 'Waiting for PostgreSQL...'
    sleep 0.1
done

echo 'PostgreSQL started'
# Run Locust in the background
# echo 'Starting Locust...'
# pwd
# locust -f locust.py --host 0.0.0.0:8090 &

cd /app/backend

echo 'Running migrations...'
python manage.py migrate

echo 'Collecting static files...'
python manage.py collectstatic --no-input


echo 'Starting Gunicorn server...'
exec gunicorn root.wsgi:application --bind 0.0.0.0:8000 --workers 6 --threads 10