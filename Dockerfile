FROM python:3.6-alpine


ADD sheet
ADD requirements.txt /
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "./streaming.py"]