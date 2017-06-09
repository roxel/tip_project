import requests
import datetime
from bs4 import BeautifulSoup
from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/<path:website>')
def index(website='http://www.aeklors.com/'):
    print(website)
    return link_counter(website)


def check_website(address):
    print("checking %s" % address)
    try:
        response = requests.get(address)
    except requests.ConnectionError:
        return []
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.findAll('a', href=True)
    return links


def link_counter(starting_address):
    address_tested = starting_address
    started = datetime.datetime.now()

    links = check_website(address_tested)
    link_count = len(links)
    links = [link["href"] for link in links]
    for link in links:
        if "http" in link:
            level_1_links = check_website(link)
            link_count += len(level_1_links)

    finished = datetime.datetime.now()
    taken = finished - started
    message = "Link count on website {} and neighbors is {}. Time taken: {}".format(
        address_tested, link_count, taken
    )
    return message


app.run(host="0.0.0.0", port=8000, debug=True)

