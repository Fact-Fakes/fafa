release: chmod u+x release.sh && ./release.sh
web: pipenv shell && gunicorn core.wsgi:application --bind 0.0.0.0:8000