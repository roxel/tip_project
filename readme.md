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

### Demo app

Demo application is based on a Python Flask framework. It's a basic crawler/link counter. For every path received as:
`http://127.0.0.1:8080/<address-to-test>` it visits the address and all websites referenced in `<a>` tags, then it returns 
total count of all the links on those websites and time taken by this test.

App can be started in Docker container. To build image and start the application:
 
    docker build -t tip_dd .
    doc up -d
    curl "127.0.0.1:8080/http://www.google.com"

### Sender image

    docker build -t roxel/sender .
    doc up -d
    
### Receiver image

    docker build -t roxel/receiver .
    doc up -d

### Starting

Sender and Receiver use mitmproxy.
To run receiver (redirect from port 5001 to <http://localhost:8000>)

    mitmdump -s receiver.py -p 5001 -R http://localhost:8000

To run sender (redirect from port 5000 to <http://localhost:5001>)

    mitmdump -s sender.py -p 5000 -R http://localhost:5001


