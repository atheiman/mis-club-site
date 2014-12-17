#!/bin/bash

# Shell script to be executed on an Ubuntu server to update production
# and run the django site. You must already have your mysql database configured.



# Exit immediately if a command exits with a non-zero status.
#set -e



PROJ_NAME=mis-club-site
PROJ_DIR=/opt/$PROJ_NAME

GIT_PRODUCTION_BRANCH=production

VIRTUALENV=/opt/virtualenvs/$PROJ_NAME
PYTHON=$VIRTUALENV/bin/python
PIP=$VIRTUALENV/bin/pip
GUNICORN=$VIRTUALENV/bin/gunicorn

DJANGO_MANGT_FILE=$PROJ_DIR/manage.py
DJANGO_MANGT_VERBOSITY=2
REQUIREMENTS_FILE=$PROJ_DIR/conf/requirements.txt
PROD_SETTINGS_PY_PATH=settings.prod
PROD_SETTINGS_FILE=$PROJ_DIR/settings/prod.py

DATADUMP=/tmp/$PROJ_NAMEdatadump.json

GUNICORN_CONFIG=$PROJ_DIR/conf/config.wsgi

NGINX_SITE_CONF=$PROJ_DIR/conf/nginx_site_config
NGINX_CONF_DIR=/etc/nginx

STATIC_ROOT=$PROJ_DIR/static_root



pretty_print() {
    echo -e "\n\n--$MESSAGE--\n"
}



# Stop running services
MESSAGE="STOPPING NGINX AND GUNICORN"; pretty_print
pkill --full $PROJ_NAME
nginx -s quit
pkill nginx



# Install OS Level Packages
MESSAGE="INSTALLING OS LEVEL PACKAGES"; pretty_print
apt-get update
apt-get install --yes mysql-client libmysqlclient-dev python-dev python-pip nginx



# Update the source
MESSAGE="UPDATING $PROJ_NAME SOURCE"; pretty_print
cd $PROJ_DIR
git checkout -- $PROJ_DIR
git checkout $GIT_PRODUCTION_BRANCH
git pull origin $GIT_PRODUCTION_BRANCH
chmod --recursive --verbose a+rx $PROJ_DIR



# Setup a virtualenv
MESSAGE="SETTING UP VIRTUALENV"; pretty_print
# If a virtualenv does not exist, then create it
if [ ! -d "$VIRTUALENV" ]; then
    virtualenv $VIRTUALENV
fi
$PIP install --requirement=$REQUIREMENTS_FILE --upgrade --verbose



# Create a copy of the data just to be safe
MESSAGE="MIGRATING DATABASE"; pretty_print
$PYTHON $DJANGO_MANGT_FILE dumpdata --settings=$PROD_SETTINGS_PY_PATH --verbosity=$DJANGO_MANGT_VERBOSITY > $DATADUMP
# Migrate the database
$PYTHON $DJANGO_MANGT_FILE migrate --settings=$PROD_SETTINGS_PY_PATH --verbosity=$DJANGO_MANGT_VERBOSITY



# Prepare static files
MESSAGE="PREPARING STATIC FILES"; pretty_print
rm --recursive --force --verbose $STATIC_ROOT
mkdir --verbose --parents $STATIC_ROOT/static
# collect all apps static files to one dir for serving
$PYTHON $DJANGO_MANGT_FILE collectstatic --settings=$PROD_SETTINGS_PY_PATH --noinput --clear --verbosity=$DJANGO_MANGT_VERBOSITY



# Run gunicorn to serve django site
MESSAGE="LAUNCHING GUNICORN"; pretty_print
rm --force --verbose /tmp/gunicorn*
# TODO: nohup gunicorn
# nohup gunicorn > /dev/null 2>&1 &
$GUNICORN --config=$GUNICORN_CONFIG conf.wsgi &
# $GUNICORN --pid /tmp/gunicorn_pid --access-logfile /tmp/gunicorn.access.log --error-logfile /tmp/gunicorn.error.log --bind unix:/tmp/gunicorn.sock conf.wsgi &




# Configure nginx to proxy django site and serve static files
MESSAGE="CONFIGURING AND LAUNCHING NGINX"; pretty_print
rm --force --verbose $NGINX_CONF_DIR/sites-*/$PROJ_NAME
cp --verbose $NGINX_SITE_CONF $NGINX_CONF_DIR/sites-available/$PROJ_NAME
ln --symbolic --verbose $NGINX_CONF_DIR/sites-available/$PROJ_NAME $NGINX_CONF_DIR/sites-enabled/$PROJ_NAME
nginx
