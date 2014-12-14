#!/bin/bash

# Shell script to be executed on a server to update production and run the django app

PROJ_NAME=mis-club-site
PROJ_DIR=/opt/$PROJ_NAME

GIT_PRODUCTION_BRANCH=production

VIRTUAL_ENV=/opt/virtualenvs/$PROJ_NAME
DJANGO_MANGT_FILE=$PROJ_DIR/manage.py
REQUIREMENTS_FILE=$PROJ_DIR/conf/requirements.txt
PROD_SETTINGS_PY_PATH=settings.prod
PROD_SETTINGS_FILE=$PROJ_DIR/settings/prod.py

DATADUMP=/tmp/$PROJ_NAME_datadump.json

VHOST_NAME=$PROJ_NAME.conf
APACHE_VHOST_CONF=$PROJ_DIR/conf/$VHOST_NAME
APACHE_SITES_AVAIL_DIR=/etc/apache2/sites-available

LIGHTTPD_CONF=$PROJ_DIR/conf/lighttpd_conf
LIGHTTPD_CONF_INCLUDES=/etc/lighttpd/includes
STATIC_ROOT=/var/www/django-static/$PROJ_NAME



# Stop running services
service apache2 stop
service lighttpd stop



# Update the source
cd $PROJ_DIR
git checkout $GIT_PRODUCTION_BRANCH
git pull origin $GIT_PRODUCTION_BRANCH
chmod --recursive a+rx $PROJ_DIR



# Setup a virtualenv
rm --recursive --force --verbose $VIRTUAL_ENV
virtualenv $VIRTUAL_ENV
source $VIRTUAL_ENV/bin/pip install --requirement=$REQUIREMENTS_FILE



# Create a copy of the data just to be safe
$VIRTUAL_ENV/bin/python $DJANGO_MANGT_FILE dumpdata --settings=$PROD_SETTINGS_PY_PATH > $DATADUMP
# Migrate the database
$VIRTUAL_ENV/bin/python $DJANGO_MANGT_FILE migrate --settings=$PROD_SETTINGS_PY_PATH



# Serve static files with Lighttpd
rm --recursive --force --verbose $STATIC_ROOT
mkdir --verbose $STATIC_ROOT
$VIRTUALENV/bin/python $PROJ_DIR/manage.py collectstatic --settings=$PROD_SETTINGS_PY_PATH --noinput --clear
rm --force --verbose $LIGHTTPD_CONF_INCLUDES/$PROJ_NAME
cp --verbose $LIGHTTPD_CONF $LIGHTTPD_CONF_INCLUDES/$PROJ_NAME
chmod --verbose a+rx $LIGHTTPD_CONF_INCLUDES/$PROJ_NAME
service lighttpd start



# Run Django site using Apache mod_wsgi
rm --force --verbose $APACHE_SITES_AVAIL_DIR/$VHOST_NAME
cp --verbose $APACHE_VHOST_CONF $APACHE_SITES_AVAIL_DIR/$VHOST_NAME
a2ensite $VHOST_NAME
service apache2 start
