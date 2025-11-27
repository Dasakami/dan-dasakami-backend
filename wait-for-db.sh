#!/bin/sh
echo "Waiting for postgres..."
while ! pg_isready -h $DB_HOST -p 5432 -U $DB_USER; do
  sleep 1
done
echo "Postgres is ready, starting Gunicorn..."
exec gunicorn dan_dasakami.wsgi:application --bind 0.0.0.0:8000 --timeout 120
