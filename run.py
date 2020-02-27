#!/usr/bin/env python3
import json
import sys

import verifier

BAD_JSON = "BAD_JSON"
BAD_VERIFIER = "VERIFIER_ERROR"
OK = "OK"


def protocol(message, verify_function=verifier.verify):
    try:
        content = json.loads(message)
    except Exception as j:
        return create_reply(BAD_JSON, str(j))
    try:
        errs = verify_function(message)
    except Exception as v:
        return create_reply(BAD_VERIFIER, "Verifier exception: {!r}".format(v))
    if not isinstance(errs, list):
        return create_reply(BAD_VERIFIER, "Verifier must return a list of strings, not a {!s}".format(type(errs)))

    for i, s in enumerate(errs):
        if not isinstance(s, str):
            return create_reply(BAD_VERIFIER,
                                "Non string object in list -- element {} has type {} instead.".format(i,type(s)))

    return create_reply(OK, errs)


def create_reply(status, details):
    return json.dumps({"status": status, "details": details})


def serve(in_=sys.stdin, out=sys.stdout):
    request = read_message(in_)
    reply = protocol(request)
    write_message(out, reply)


def read_message(filehandle):
    buf = ""
    for data in filehandle.read():
        buf += data
    return buf


def write_message(filehandle, message):
    filehandle.write(message)
    print(message)


if __name__ == "__main__":
    serve()
