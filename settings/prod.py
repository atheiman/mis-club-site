# prod is for running the server on the production webserver

from .common import *
from .private import PROD_DB, PROD_SECRET_KEY

SECRET_KEY = PROD_SECRET_KEY

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['.austinheiman.com']

DATABASES = PROD_DB

STATIC_URL = 'http://mis-club.austinheiman.com:/static/'

# Gunicorn settings
pid = "/tmp/gunicorn.pid"
accesslog = "/tmp/gunicorn.access.log"
errorlog = "/tmp/gunicorn.error.log"
bind = "unix:/tmp/gunicorn.sock"
