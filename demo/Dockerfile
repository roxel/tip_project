FROM python:latest
MAINTAINER Piotr Roksela <piotr@roksela.pl>

ENV APP_DIR=/home/dd \
    APP_PORT=8000

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

COPY . $APP_DIR

WORKDIR $APP_DIR

VOLUME ["$APP_DIR"]
EXPOSE $APP_PORT

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["python"]
