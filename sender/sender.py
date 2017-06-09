from datetime import datetime
import json
from mitmproxy import http
import random

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


def time_difference(time_str, time_datetime):
    time_app_outgoing = str_to_tip_time(time_str)
    return time_datetime - time_app_outgoing


def time_difference_str(t1_str, t2_str):
    t1 = str_to_tip_time(t1_str)
    t2 = str_to_tip_time(t2_str)
    return t2 - t1


def time_measure():
    if random.uniform(0.0, 1.0) <= 0.2:
        return True
    else:
        return False


def request(flow: http.HTTPFlow) -> None:
    "time before passing to receiver"
    #if time_measure():
      #  print("TIME_INCOMING_ADDED")
    flow.request.headers[TIP_INCOMING] = tip_time_to_str()


def response(flow: http.HTTPFlow) -> None:
    """time after coming from application"""
    # flow.response.headers["TIP-Received"] = tip_time()
    if TIP_APP_OUTGOING in flow.response.headers:
        r2s_time = time_difference(
            time_str=flow.response.headers.get(TIP_APP_OUTGOING),
            time_datetime=datetime.now(),
        )
        print("R->S time: {}".format(r2s_time))
        s2r_time = time_difference_str(
            t1_str=flow.response.headers.get(TIP_INCOMING),
            t2_str=flow.response.headers.get(TIP_APP_INCOMING),
        )
        print("S->R time: {}".format(s2r_time))


