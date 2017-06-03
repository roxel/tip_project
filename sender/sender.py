from datetime import datetime
import json
from mitmproxy import http


def tip_time():
    return str(datetime.now())


def request(flow: http.HTTPFlow) -> None:
    "time before passing to receiver"
    flow.request.headers["TIP-Incoming"] = tip_time()
    print(json.dumps(dict(flow.request.headers)))


def response(flow: http.HTTPFlow) -> None:
    "time after coming from application"
    flow.response.headers["TIP-Outgoing"] = tip_time()
    print(json.dumps(dict(flow.response.headers)))





# mitmdump -s sender.py -p 5000 -R http://localhost:5001


# mitmdump -R http://localhost:5001 --setheader :~q:Host:localhost:5001 --setheader :~q:TipHeader:20 -p 5000



