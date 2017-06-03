from datetime import datetime
import json
from mitmproxy import http


def tip_time():
    return str(datetime.now())


def request(flow: http.HTTPFlow) -> None:
    "time before passing to application"
    flow.request.headers["TIP-App-Incoming"] = tip_time()
    print(json.dumps(dict(flow.request.headers)))


def response(flow: http.HTTPFlow) -> None:
    "time after coming from application"
    flow.response.headers["TIP-App-Outgoing"] = tip_time()
    print(json.dumps(dict(flow.response.headers)))


# mitmdump -s receiver.py -p 5001 -R http://localhost:8000




