PROJ_NAME=mis-club-site
$PROJ_DIR=/opt/$PROJ_NAME
VIRTUAL_ENV=/opt/virtualenvs/$PROJ_NAME
REQUIREMENTS_FILE=$PROJ_DIR/conf/requirements.txt

rm -rf $VIRTUAL_ENV
virtualenv $VIRTUAL_ENV
source $VIRTUAL_ENV/bin/pip install --requirement=$REQUIREMENTS_FILE
