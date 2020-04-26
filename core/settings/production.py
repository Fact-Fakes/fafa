"""
PRODUCTION SETTINGS

GET VARIABLES FROM ENVIRON
os.environ.get('variable')
"""
from core.settings.core import *
import dj_database_url
import os


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG")

ALLOWED_HOSTS = ["0.0.0.0", "localhost", "127.0.0.1", "fafaapp.herokuapp.com"]


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# PostrgSQL heere
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DATABASE_DB"),
        "USER": os.environ.get("DATABASE_USER"),
        "PASSWORD": os.environ.get("DATABASE_PASS"),
        "HOST": os.environ.get("DATABASE_HOST"),
        "PORT": os.environ.get("DATABASE_PORT"),
    }
}
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

CORS_ORIGIN_ALLOW_ALL = True
