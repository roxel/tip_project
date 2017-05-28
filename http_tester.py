from urllib import request


if __name__ == "__main__":
    host, port = "127.0.0.1", 8080

    address = "http://{}:{}".format(host, port)
    response = request.urlopen(address).read()
    print(response)

