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
RUN mkdir /code/db
RUN python manage.py collectstatic --noinput
EXPOSE 80
ADD start.sh /code/
VOLUME ["/code/db",]
ENTRYPOINT /code/start.sh