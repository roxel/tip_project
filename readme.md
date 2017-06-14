TIP Project
=====

Docker containers for measuring application processing times and HTTP traffic delays. 

## Solution

* Two proxies added on path from to client to server. First container, Sender on the same machine as the client, 
and second container, Receiver somewhere close the server.
* The server isn't aware that the traffic is monitored - nothing changes in its setup. 
The client must only change destination address to host:port address of the Sender.
* Every HTTP request received by Sender is sent to the Receiver. Every few requests HTTP header is added with time 
when Sender received the request.
* Receiver passes requests to server application and then returns responses to the Sender with timestamp before and after
the request was processed by the application.


Parameters monitored:

* time of transmission from client to server (Sender to Receiver)
* application processing time (Receiver to Receiver)
* time of transmission from server to client (Receiver to Sender)

Statistics are generated as csv file on the machine where Sender is running.

Both the Sender and the Receiver are based on mitmproxy <https://github.com/mitmproxy/mitmproxy/>.

## Code

The solution consists of two apps isolated as docker containers: Sender and Receiver.
Docker Compose can be used to access the containers. 

### Sender image

Building Sender image and starting container:

    docker build -t tip_sender .
    doc up -d
    
Sender is configured for Receiver running on the same machine by default (`http://127.0.0.1:5001`). It will not work 
when Receiver is started inside container or on another machine. First you must change Receiver address.
The Receiver address can be changed in `docker-compose.yml` file by changing command: 

    mitmdump -s sender.py -p 5000 -R <receiver host:port address>
    
### Receiver image

Building Receiver image and starting container:

    docker build -t tip_receiver .
    doc up -d
    
Receiver is configured for server application running on the same machine by default (`http://127.0.0.1:8000`). 
It will not work when application is started inside container. First you must change Receiver address.
The application address can be changed in `docker-compose.yml` file by changing command: 

    mitmdump -s sender.py -p 5000 -R <receiver host:port address>
    
### Demo app

Demo application is based on a Python Flask framework. It's a basic crawler/link counter. For every path received as:
`http://127.0.0.1:8080/<address-to-test>` it visits the address and all websites referenced in `<a>` tags, then it returns 
total count of all the links on those websites and time taken by this test.

App can be started in Docker container. To build image and start the application:
 
    docker build -t tip_dd .
    doc up -d
    curl "127.0.0.1:8080/http://www.google.com"

### Troubleshooting

* Sometimes the demo application block on incoming requests for a long time. 
Application requests, by design, take 30-60s seconds on average websites for good internet connection.



