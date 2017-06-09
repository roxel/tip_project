FROM mitmproxy/mitmproxy
MAINTAINER Piotr Roksela <piotr@roksela.pl>

ENV APP_DIR=/home/sender \
    APP_PORT=5000

COPY . $APP_DIR

COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

VOLUME ["$APP_DIR"]
EXPOSE $APP_PORT

WORKDIR $APP_DIR
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["sender"]
