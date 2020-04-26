pip install pipenv
pipenv install
pipenv install gunicorn
pipenv shell

python manage.py flush --no-input --settings=core.settings.production
python manage.py migrate --settings=core.settings.production
python manage.py load_excel --settings=core.settings.production