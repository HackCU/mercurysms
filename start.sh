#!/bin/sh

python manage.py migrate --noinput
python manage.py initadmin
gunicorn -b 0.0.0.0:80 mercurysms.wsgi --log-file -