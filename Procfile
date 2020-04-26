release: chmod u+x release.sh && ./release.sh
web: pipenv run gunicorn core.wsgi:application --bind 0.0.0.0:8000