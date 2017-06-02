TIP Project
=====

The solution consists of two apps isolated as docker containers: sender and receiver.
Docker Compose can be used to access the containers. 

## Demo app

Demo app is a Python Django application running in Docker container. To build the image and start application:
 
    docker build -t roxel/dd .
    doc up -d
    curl "127.0.0.1:8080/polls/"

## Sender image

    docker build -t roxel/sender .
    doc up -d
    

## Docker bridge network for local simulation 

This way they will both join the same bridge network
and will be able to access themselves directly using TCP/IP communication.

To verify that they are connected:

1. Start sender.


    cd sender
    docker-compose up -d

2. Check its IP address.


    docker inspect sender_sender_1
    ... # in returned json config find IPAddress, e.g.:
    
                    "Gateway": "172.20.0.1",
                    "IPAddress": "172.20.0.2",
                    "IPPrefixLen": 16,


    
3. Start the receiver and ping correct address.


    doc run --service-ports receiver sh
    / # ping 172.20.0.2


### Starting `sender` as TCP bridge

1st shell:

    cd demo
    docker build -t roxel/dd .
    doc up

Django application is now running on port 8080 of the host system.
In 2nd shell do:

    cd sender
    python sender.py
    
TCP server is now running on port 5000.
Now in 3rd shell:

    python http_tester.py
    
or:

    python tcp_tester.py
    
When testers are run, they should issue proper type of request to localhost:5000. 
Sender passes them forward to django application and returns response from there.
Unfortunately, nothing is returned... Just `b''` in case of use http_tester.py 
(because django understands request and answers but Sender can get the response). 
In this scenerio tcp_tester.py don't get any response, because django only answers HTTP.

