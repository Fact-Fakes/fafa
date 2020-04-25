[![Pipeline](https://circleci.com/gh/Fact-Fakes/fafa.svg?style=svg&circle-token=332391ed813d822c77ef1801908774689db89b25)](https://app.circleci.com/pipelines/github/Fact-Fakes/fafa)
[![Codecov](https://codecov.io/gh/Fact-Fakes/fafa/branch/master/graph/badge.svg?token=aJNPKNp0Fn)](https://codecov.io/gh/Fact-Fakes/fafa)




# FAFA

This is repository for awesome project named FAFA developed for [HackCrisis hackathon](https://www.hackcrisis.com/)

This project is written in Django (+ Django REST Framework) and React

## Prerequisites

 - [Docker](https://www.docker.com/) (Use this for fast setup of app)
 - [Yarn](https://classic.yarnpkg.com/en/)
 - [Python 3.8](https://www.python.org/)
 - [Pipenv](https://github.com/pypa/pipenv) 

## Running app in production mode
Running in production mode requires [Docker](https://www.docker.com/) 

- Run in root folder `docker-compose up -d --build`

## Running app in development mode

### Backend (Django with Django REST Framework)

> To run with docker go to `dockerfiles/backend/` and run `docker-compose up -d --build`

 1. In root directory install packages  `pipenv install`
 2. Open virtual environment `pipenv shell`
 3. Make migrations `python manage.py makemigrations`
 4. Migrate `python manage.py migrate`
 5. Load content from excel file `python manage.py load_excel`
 6. Start Django server `python manage.py runserver`

### Frontend (React)

> To use docker, in root directory run `docker-compose up -d --build`

1. In `frontend/` directory run `yarn install`
2. Run `yarn start` to launch development server

## Endpoints
Backend contains 4 endpoints

#### 1. Getting question list

 - URL
`/questions/?format=json`
- Method
`GET`
- URL Params

`sessionID` -> SessionID cookie to identify user

`search` -> String to search among title and keywords

`page` -> Number of page


#### 2. Getting specify question

 - URL
`/questions/<INT:PK>/?format=json`
- Method
`GET`
- URL Params

`sessionID` -> SessionID cookie to identify user

#### 3. Add answer to question

 - URL
`/answer/add/`
- Method
`POST`
- POST Params

`question` -> ID of question to answer (required)

`sessionID` -> SessionID cookie to identify user

`users_answer` -> Bool if answer is YES (true) or NO (false)

#### 4 Add vote for question

 - URL
`/vote/add/`
- Method
`POST`
- POST Params

`question` -> ID of question to answer (required)

`sessionID` -> SessionID cookie to identify user

`updown` -> Bool if vote is UP (true) or DOWN (false)
