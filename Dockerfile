FROM tiangolo/uwsgi-nginx-flask:flask-python3.5

MAINTAINER Laurent Rivard <laurentrivard@gmail.com>

COPY . /wristlock

WORKDIR /wristlock

RUN pip install -r requirements.txt

CMD bash start.sh
