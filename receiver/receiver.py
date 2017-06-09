from datetime import datetime
import json
from datetime import datetime
from mitmproxy import http


TIP_INCOMING = "TIP-Incoming"
TIP_APP_INCOMING = "TIP-App-Incoming"
TIP_OUTGOING = "TIP-Outgoing"
TIP_APP_OUTGOING = "TIP-App-Outgoing"

time_format = "%Y-%m-%d %H:%M:%S.%f"


def tip_time_to_str(d):
    return d.strftime(time_format)


def str_to_tip_time(time_str):
    return datetime.strptime(time_str, time_format)


def time_difference(time_str, time_datetime):
    time_app_outgoing = str_to_tip_time(time_str)
    return time_datetime - time_app_outgoing


def time_difference_str(t1_str, t2_str):
    t1 = str_to_tip_time(t1_str)
    t2 = str_to_tip_time(t2_str)
    return t2 - t1


def request(flow: http.HTTPFlow) -> None:
    """time before passing to application"""
    if TIP_INCOMING in flow.request.headers:
        flow.tip_incoming = datetime.now()
    # print(json.dumps(dict(flow.request.headers)))


def response(flow: http.HTTPFlow) -> None:
    """time after coming from application"""
    if TIP_INCOMING in flow.request.headers:
        flow.response.headers[TIP_APP_OUTGOING] = tip_time_to_str(datetime.now())
        flow.response.headers[TIP_APP_INCOMING] = tip_time_to_str(flow.tip_incoming)
        flow.response.headers[TIP_INCOMING] = flow.request.headers[TIP_INCOMING]
        print(datetime.now() - flow.tip_incoming)

# mitmdump -s receiver.py -p 5001 -R http://localhost:8000




