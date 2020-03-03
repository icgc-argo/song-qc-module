#!/usr/bin/env python3
import json
import sys

import verifier

ERROR = "VERIFIER_ERROR"
ISSUES = "ISSUES"
OK = "OK"


def protocol(message, verify_function=verifier.verify):
    if not message:
        return create_reply(ISSUES, ["NO JSON: Received empty message"])
    try:
        json.loads(message)
    except Exception as j:
        return create_reply(ISSUES, ["BAD JSON: " + str(j)])

    try:
        errs = verify_function(message)
    except Exception as v:
        return create_reply(ERROR, ["Verifier exception: {!r}".format(v)])
    if not isinstance(errs, list):
        return create_reply(ERROR, ["Verifier must return a list of strings, not a {!s}".format(type(errs))])

    for i, s in enumerate(errs):
        if not isinstance(s, str):
            return create_reply(ERROR,
                                ["Non string object in list -- element {} has type {} instead.".format(i, type(s))])
    if errs:
        return create_reply(ISSUES, errs)
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


if __name__ == "__main__":
    serve()
