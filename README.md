[![Pipeline](https://gitlab.com/daniel.rozycki/fakebuster/badges/master/pipeline.svg)](https://gitlab.com/daniel.rozycki/fakebuster) 
[![Coverage](https://gitlab.com/daniel.rozycki/fakebuster/badges/master/coverage.svg)](https://gitlab.com/daniel.rozycki/fakebuster)


# FakeBuster

This is repository for awesome project named FakeBuster


# Prerequisites

 - Python 3.8 (`sudo apt install python3.8`)
 - Pipenv (`python3.8 -m pip install pipenv`) 

# Running

> Default settings are `core/settings/development` if You wish to change the settings use this command: `python manage.py runserver --settings=core.settings.production`

 1. Install packages from Pipfile `pipenv install`
 2. Open virtual environment `pipenv shell`
 3. Create migrations `python manage.py makemigrations`
 4. Migrate `python manage.py migrate`
 5. Load data from questions.xlsx `python manage.py load_excel`
 6. Start Django server `python manage.py runserver`
 7. Go to `localhost:8000` to see main page
 > To add package run e.g. `pipenv install package_name`

# Endpoints

### Getting questions
*  ***URL***
`/questions/?format=json`

*  ***URL PARAMS***
`sessionID=string max 255` -> By adding this param We can get user answers (Use as required)

`search=string` -> This will search in title and keywords of questions

Above params can be chained e.g. `/questions/?format=json&sessionID=sampleid&search=samplesearch`

### Getting one question

*  ***URL***
`/questions/<QUESTION_ID:INTEGER>/`

* ***URL PARAMS**
Same as above