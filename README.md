# FakeBuster

This is repository for awesome project named FakeBuster


# Prerequisites

 - Python 3.8 (`sudo apt install python3.8`)
 - Pipenv (`python3.8 -m pip install pipenv`) 

# Running

> Default settings are `core/settings/development` if You wish to change the settings use this command: `python manage.py runserver --settings=core.settings.production`

 1. Install packages from Pipfile `pipenv install`
 2. Open virtual environment `pipenv shell`
 3. Start Django server `python manage.py runserver`
 > To add package run e.g. `pipenv install package_name`