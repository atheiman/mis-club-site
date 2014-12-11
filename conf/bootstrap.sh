#!/usr/bin/env bash



# Shell script to deploy mis-club-site to an Ubuntu server.



# Global vars
PROJ_NAME=mis-club-site
PROJ_DIR=/opt/$PROJ_NAME
TEMP_DIR=/tmp/$PROJ_NAME

DEV_DB=$PROJ_DIR/db.sqlite3

VIRTUALENV=$PROJ_DIR/env
REQUIREMENTS_FILE=$PROJ_DIR/conf/requirements.txt

GITHUB_RELEASE_TAG=1.1.0
GITHUB_RELEASE_URL=https://github.com/atheiman/mis-club-site/archive/$GITHUB_RELEASE_TAG.tar.gz

WSGI_RELATIVE_PATH=conf/wsgi.py
APACHE_VHOST_CONF=$PROJ_DIR/conf/vhost_config
APACHE_CONF_DIR=/etc/apache2
APACHE_VHOST=misclub

LIGHTTPD_CONF=$PROJ_DIR/conf/lighttpd.conf
LIGHTTPD_CONF_DIR=/etc/lighttpd
STATIC_ROOT=$PROJ_DIR/staticfiles



# Clean up from previous provisions
rm -rf $PROJ_DIR $TEMP_DIR
mkdir $TEMP_DIR



# Install OS packages
apt-get update
apt-get install --yes python-pip apache2 libapache2-mod-wsgi lighttpd



# Get the source from Github
#wget --directory-prefix=$TEMP_DIR/ $GITHUB_RELEASE_URL
#tar -xzf $TEMP_DIR/$GITHUB_RELEASE_TAG.tar.gz -C $TEMP_DIR
#mv $TEMP_DIR/$PROJ_NAME-$GITHUB_RELEASE_TAG $PROJ_DIR

# Copy the source from the vagrant shared folder
mkdir $PROJ_DIR
cp -r /vagrant/* $PROJ_DIR/



# Setup a virtualenv
pip install virtualenv
virtualenv $VIRTUALENV
$VIRTUALENV/bin/pip install --requirement=$REQUIREMENTS_FILE



# Apply any needed migrations
$VIRTUALENV/bin/python $PROJ_DIR/manage.py migrate
chgrp --recursive www-data $PROJ_DIR
chmod --recursive 775 $PROJ_DIR
# $VIRTUALENV/bin/python $PROJ_DIR/manage.py runserver 0.0.0.0:8000



# Lighttpd Static File Server Config

# Create an empty dir to hold static files
mkdir $STATIC_ROOT
# Collect static files for all apps into settings.STATIC_ROOT
$VIRTUALENV/bin/python $PROJ_DIR/manage.py collectstatic --noinput --clear
# Allow apache to access static files
chmod --recursive 755 $STATIC_ROOT

# Config lighttpd to serve static files
rm -rf $LIGHTTPD_CONF_DIR/lighttpd.conf
cp $LIGHTTPD_CONF $LIGHTTPD_CONF_DIR/lighttpd.conf
# Run lighttpd
/etc/init.d/lighttpd start



# Apache HTTP Server Config

# Clear virtual hosts
rm -rf $APACHE_CONF_DIR/sites-*/*

# Create a Django virtual host
cp $APACHE_VHOST_CONF $APACHE_CONF_DIR/sites-available/$APACHE_VHOST

# Enable the Django virtual host
a2ensite $APACHE_VHOST
service apache2 restart
