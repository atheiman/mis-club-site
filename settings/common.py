"""
Django settings for MIS Club Site project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

PROJ_NAME = 'mis-club-site'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# The below secret key will only be used in dev and qa (running the server locally)
SECRET_KEY = '&5jrp(21$upx!r!kd_nil1y=%vgt)idw0!j0+0o+-vlp*4toy9'


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'attendance',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'conf.urls'

WSGI_APPLICATION = 'conf.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

# string representing the language code for this installation
LANGUAGE_CODE = 'en-us'

# string representing the time zone for this installation
TIME_ZONE = 'America/Chicago'

# Django translation system
USE_I18N = True

# localized formatting of data
USE_L10N = True

# datetimes will be timezone-aware by default or not
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# collectstatic will dump a dir full of static files for each app here
STATIC_ROOT = os.path.join(BASE_DIR, "static_root/static")

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)
