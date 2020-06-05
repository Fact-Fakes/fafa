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
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get("DEBUG"))

ALLOWED_HOSTS = ["0.0.0.0", "localhost", "127.0.0.1", "fafaapi.altosterino.com"]


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
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# DEFAULT_FILE_STORAGE = "storages.backends.dropbox.DropBoxStorage"
# DROPBOX_OAUTH2_TOKEN = os.environ.get("DROPBOX_TOKEN")


REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
}


CORS_ORIGIN_ALLOW_ALL = True
