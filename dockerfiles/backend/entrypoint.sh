#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

pipenv run python manage.py flush --no-input --settings=core.settings.production
pipenv run python manage.py migrate --settings=core.settings.production
pipenv run python manage.py load_excel --settings=core.settings.production
pipenv run python manage.py collectstatic --no-input

exec "$@"