FROM python:3.6-alpine

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD manage.py /code/
RUN mkdir /code/mercurysms
RUN mkdir /code/authmanager
ADD mercurysms /code/mercurysms
ADD authmanager /code/authmanager

RUN python manage.py migrate --noinput
RUN python manage.py initadmin
RUN python manage.py collectstatic --noinput
EXPOSE 80
VOLUME ["/code/db.sqlite3",]
ENTRYPOINT ["gunicorn", "-b 0.0.0.0:80", "mercurysms.wsgi", " --log-file -"]