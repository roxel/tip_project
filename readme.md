TIP Project
=====

The solution consists of two apps isolated as docker containers: sender and receiver.
Docker Compose can be used to access the containers. This way they will both join the same bridge network
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


