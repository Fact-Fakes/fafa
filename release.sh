pip install --upgrade pip
pip install --upgrade pipenv
pipenv install
pipenv install gunicorn
pip install gunicorn

pipenv run python manage.py flush --no-input --settings=core.settings.production
pipenv run python manage.py migrate --settings=core.settings.production
pipenv run python manage.py load_excel --settings=core.settings.production