import os

"""
PRODUCTION SETTINGS

GET VARIABLES FROM ENVIRON
os.environ.get('variable')
"""
from core.settings.core import *
import os


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "verysecretkey"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["allowedhost"]


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# PostrgSQL heere
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
