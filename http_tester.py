from urllib import parse, request
import requests


if __name__ == "__main__":
    host, port = "127.0.0.1", 5000
    values = {'name': 'Marcin'
              }

    address = "http://{}:{}".format(host, port)
    data = parse.urlencode(values).encode('ascii')
    req = request.Request(address, data)
    response = request.urlopen(req).read()
    print(response)

