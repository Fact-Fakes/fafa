FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN mkdir /api

WORKDIR /api

ADD backend /api/backend
ADD core /api/core
ADD manage.py /api/
ADD Pipfile /api/
ADD dockerfiles/backend/entrypoint.sh /api/
ADD questions.xlsx /api/

RUN chmod +x entrypoint.sh

RUN pip install pipenv && pipenv install && pipenv install psycopg2 && pipenv install gunicorn

ENTRYPOINT ["/api/entrypoint.sh"]