#!/usr/bin/env bash



# Shell script to deploy mis-club-site to a vm provisioned by vagrant.



# Global vars
PROJ_NAME=mis-club-site
PROJ_DIR=/opt/$PROJ_NAME
TEMP_DIR=/tmp/$PROJ_NAME

VIRTUALENV=$PROJ_DIR/env
REQUIREMENTS_FILE=$PROJ_DIR/conf/requirements.txt

GIT_CLONE_URL=git@github.com:atheiman/mis-club-site.git
GIT_BRANCH=tag/1.0.1

WSGI_RELATIVE_PATH=conf/wsgi.py
APACHE_VHOST=misclub
APACHE_SITES_AVAILABLE_DIR=/etc/apache2/sites-available



# clean up from previous provisions
rm -rf $PROJ_DIR $TEMP_DIR /etc/apache2/sites-enabled/*
mkdir $PROJ_DIR $TEMP_DIR



# Install OS packages
apt-get update
apt-get install --yes python-pip apache2 libapache2-mod-wsgi git



# # Get the source
git clone --branch=$GIT_BRANCH $GIT_CLONE_URL $PROJ_DIR



# # Setup a virtualenv
pip install virtualenv
virtualenv $VIRTUALENV
$VIRTUALENV/bin/pip install --requirement=$REQUIREMENTS_FILE



$VIRTUALENV/bin/python $PROJ_DIR/manage.py runserver 0.0.0.0:8000



# # Apache HTTP Server config
# rm -rf /etc/apache2/sites-enabled/*


# # Create a Django virtual host
# echo "" > $APACHE_SITES_AVAILABLE_DIR/$APACHE_VHOST

# cat <<EOT >> $APACHE_SITES_AVAILABLE_DIR/$APACHE_VHOST
# <VirtualHost *:80>

#     WSGIDaemonProcess $DJANGO_PROJECT python-path=$DJANGO_PROJECT_DIR/$DJANGO_PROJECT:$DJANGO_PROJECT_DIR/$VIRTUAL_ENV/lib/python2.7/site-packages
#     WSGIProcessGroup $DJANGO_PROJECT
#     WSGIScriptAlias / $DJANGO_PROJECT_DIR/$DJANGO_PROJECT/$WSGI_RELATIVE_PATH

#     ServerAdmin atheimanksu@gmail.com

#     ErrorLog ${APACHE_LOG_DIR}/error.log

#     LogLevel warn

#     CustomLog ${APACHE_LOG_DIR}/access.log combined

# </VirtualHost>
# EOT

# # Enable your Django virtual host
# a2ensite $APACHE_VHOST
# service apache2 restart
