#!/usr/bin/env bash



# Shell script to deploy mis-club-site to a vm provisioned by vagrant.



# Global vars
PROJ_NAME=mis-club-site
PROJ_DIR=/opt/$PROJ_NAME
TEMP_DIR=/tmp/$PROJ_NAME

VIRTUALENV=$PROJ_DIR/env
REQUIREMENTS_FILE=$PROJ_DIR/conf/requirements.txt

GITHUB_RELEASE_TAG=1.0.1
GITHUB_RELEASE_URL=https://github.com/atheiman/mis-club-site/archive/$GITHUB_RELEASE_TAG.tar.gz

WSGI_RELATIVE_PATH=conf/wsgi.py
APACHE_VHOST=misclub
APACHE_SITES_AVAILABLE_DIR=/etc/apache2/sites-available



# clean up from previous provisions
rm -rf $PROJ_DIR $TEMP_DIR /etc/apache2/sites-enabled/*
mkdir $TEMP_DIR



# Install OS packages
apt-get update
apt-get install --yes python-pip apache2 libapache2-mod-wsgi



# Get the source
wget --directory-prefix=$TEMP_DIR/ $GITHUB_RELEASE_URL
tar -xzf $TEMP_DIR/$GITHUB_RELEASE_TAG.tar.gz -C $TEMP_DIR
mv $TEMP_DIR/$PROJ_NAME-$GITHUB_RELEASE_TAG $PROJ_DIR



# Setup a virtualenv
pip install virtualenv
virtualenv $VIRTUALENV
$VIRTUALENV/bin/pip install --requirement=$REQUIREMENTS_FILE



# Apply any needed migrations
$VIRTUALENV/bin/python $PROJ_DIR/manage.py migrate



# $VIRTUALENV/bin/python $PROJ_DIR/manage.py runserver 0.0.0.0:8000



# Apache HTTP Server config
rm -rf /etc/apache2/sites-enabled/*


# Create a Django virtual host
echo "" > $APACHE_SITES_AVAILABLE_DIR/$APACHE_VHOST

cat <<EOT >> $APACHE_SITES_AVAILABLE_DIR/$APACHE_VHOST
<VirtualHost *:80>

    WSGIDaemonProcess $PROJ_NAME python-path=$PROJ_DIR:$VIRTUALENV/lib/python2.7/site-packages
    WSGIProcessGroup $PROJ_NAME
    WSGIScriptAlias / $PROJ_DIR/$WSGI_RELATIVE_PATH

    ServerAdmin atheimanksu@gmail.com

    ErrorLog ${APACHE_LOG_DIR}/error.log

    LogLevel warn

    CustomLog ${APACHE_LOG_DIR}/access.log combined

</VirtualHost>
EOT

# Enable your Django virtual host
a2ensite $APACHE_VHOST
service apache2 restart
