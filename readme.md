TIP Project
=====

The solution consists of two apps isolated as docker containers: sender and receiver.
Docker Compose can be used to access the containers. 

## Demo app

Demo app is a Python Django application running in Docker container. To build the image and start application:
 
    docker build -t roxel/dd .
    doc up -d
    curl "127.0.0.1:8080/http://www.google.com"

## Sender image

    docker build -t roxel/sender .
    doc up -d
    
## Receiver image

    docker build -t roxel/receiver .
    doc up -d

## Starting

Sender and Receiver use mitmproxy.
To run receiver (redirect from port 5001 to <http://localhost:8000>)

    mitmdump -s receiver.py -p 5001 -R http://localhost:8000

To run sender (redirect from port 5000 to <http://localhost:5001>)

    mitmdump -s sender.py -p 5000 -R http://localhost:5001


