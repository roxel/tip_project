FROM python:latest
MAINTAINER Piotr Roksela <piotr@roksela.pl>

COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["python"]
