
import json
import time
import pprint
import sys

# env variables contain HTTP headers and HTTP method
# req is just the body
def handle(req):
    time.sleep(15)
    pp = pprint.PrettyPrinter(indent=4)
    json_req = json.loads(req)
    pp.pprint(req.__dict__())
    return req
