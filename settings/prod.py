# prod is for running the server on the production webserver

from .common import *
from .private import PROD_DB, PROD_SECRET_KEY

SECRET_KEY = PROD_SECRET_KEY

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['austinheiman.com',]

DATABASES = PROD_DB

STATIC_URL = 'http://austinheiman.com:8000/' + PROJ_NAME + '/'
STATIC_ROOT = '/var/www/django-static/' + PROJ_NAME
