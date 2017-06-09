import json
from datetime import datetime
from mitmproxy import http

#
# starting sender:
#        mitmdump -s sender.py -p 5000 -R http://localhost:5001
#
#

TIP_INCOMING = "TIP-Incoming"
TIP_APP_INCOMING = "TIP-App-Incoming"
TIP_OUTGOING = "TIP-Outgoing"
TIP_APP_OUTGOING = "TIP-App-Outgoing"

time_format = "%Y-%m-%d %H:%M:%S.%f"


def tip_time_to_str():
    return datetime.now().strftime(time_format)


def str_to_tip_time(time_str):
    return datetime.strptime(time_str, time_format)


def request(flow: http.HTTPFlow) -> None:
    """time before passing to receiver"""
    flow.request.headers[TIP_INCOMING] = tip_time_to_str()


def response(flow: http.HTTPFlow) -> None:
    """time after coming from application"""
    # flow.response.headers["TIP-Received"] = tip_time()
    if TIP_APP_OUTGOING in flow.response.headers:
        time_now = datetime.now()
        time_str = flow.response.headers.get(TIP_APP_OUTGOING)
        time_app_outgoing = str_to_tip_time(time_str)
        time_taken = time_now - time_app_outgoing
        print("R->S time: {}".format(time_taken))


