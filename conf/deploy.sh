#!/bin/bash

# Shell script to be executed on an Ubuntu server to update production and run the django site.

PROJ_NAME=mis-club-site
PROJ_DIR=/opt/$PROJ_NAME

GIT_PRODUCTION_BRANCH=production

VIRTUAL_ENV=/opt/virtualenvs/$PROJ_NAME
DJANGO_MANGT_FILE=$PROJ_DIR/manage.py
DJANGO_MANGT_VERBOSITY=2
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



pretty_print() {
    echo -e "\n\n--$MESSAGE--\n"
}



# Stop running services
MESSAGE="STOPPING APACHE AND LIGHTTPD HTTP SERVERS"; pretty_print
service apache2 stop
pkill apache2
service lighttpd stop
pkill lighttpd



# Install OS Level Packages
MESSAGE="INSTALLING OS LEVEL PACKAGES"; pretty_print
apt-get update
apt-get install --yes mysql-server mysql-client libmysqlclient-dev python-dev python-pip apache2 libapache2-mod-wsgi lighttpd



# Update the source
MESSAGE="UPDATING $PROJ_NAME SOURCE"; pretty_print
cd $PROJ_DIR
git checkout $GIT_PRODUCTION_BRANCH
git pull origin $GIT_PRODUCTION_BRANCH
chmod --recursive --verbose a+rx $PROJ_DIR



# Setup a virtualenv
MESSAGE="SETTING UP VIRTUALENV"; pretty_print
rm --recursive --force --verbose $VIRTUAL_ENV
virtualenv $VIRTUAL_ENV
$VIRTUAL_ENV/bin/pip install --requirement=$REQUIREMENTS_FILE --upgrade --verbose



# Create a copy of the data just to be safe
MESSAGE="UPDATING DB"; pretty_print
$VIRTUAL_ENV/bin/python $DJANGO_MANGT_FILE dumpdata --settings=$PROD_SETTINGS_PY_PATH --verbosity=$DJANGO_MANGT_VERBOSITY > $DATADUMP
# Migrate the database
$VIRTUAL_ENV/bin/python $DJANGO_MANGT_FILE migrate --settings=$PROD_SETTINGS_PY_PATH --verbosity=$DJANGO_MANGT_VERBOSITY



# Serve static files with Lighttpd
MESSAGE="CONFIGURING LIGHTTPD"; pretty_print
rm --recursive --force --verbose $STATIC_ROOT
mkdir --verbose $STATIC_ROOT
# collect all apps static files to one dir for lighttpd serving
$VIRTUALENV/bin/python $DJANGO_MANGT_FILE collectstatic --settings=$PROD_SETTINGS_PY_PATH --noinput --clear --verbosity=$DJANGO_MANGT_VERBOSITY
# Add any additional lighttpd conf to the project's lighttpd conf include
rm --force --verbose $LIGHTTPD_CONF_INCLUDES/$PROJ_NAME
cp --verbose $LIGHTTPD_CONF $LIGHTTPD_CONF_INCLUDES/$PROJ_NAME
chmod --verbose a+rx $LIGHTTPD_CONF_INCLUDES/$PROJ_NAME
service lighttpd start



# Run Django site using Apache mod_wsgi
MESSAGE="CONFIGURING APACHE"; pretty_print
rm --force --verbose $APACHE_SITES_AVAIL_DIR/$VHOST_NAME
cp --verbose $APACHE_VHOST_CONF $APACHE_SITES_AVAIL_DIR/$VHOST_NAME
a2ensite $VHOST_NAME
service apache2 start
