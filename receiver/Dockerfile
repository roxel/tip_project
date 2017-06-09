FROM mitmproxy/mitmproxy

EXPOSE 5001

ENV APP_DIR=/home/receiver

COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

COPY . $APP_DIR


WORKDIR $APP_DIR

VOLUME ["$APP_DIR"]


ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["bash"]
