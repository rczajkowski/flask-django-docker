FROM python:2.7
WORKDIR /app/web

ADD . /app/web

RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD python manage.py runserver 0.0.0.0:8100