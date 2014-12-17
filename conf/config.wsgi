# Gunicorn settings

pid = "/tmp/gunicorn.pid"
accesslog = "/tmp/gunicorn.access.log"
errorlog = "/tmp/gunicorn.error.log"
bind = "unix:/tmp/gunicorn.sock"
