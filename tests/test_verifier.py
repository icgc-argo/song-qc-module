#!/usr/bin/env python3
import unittest
from os import listdir
from run import protocol

import json


class MyTestCase(unittest.TestCase):
    def test_success(self):
        failures = False
        for f in listdir("tests/passing"):
            print("Testing file {} (should pass)...".format(f))
            with open("tests/passing/" + f) as fh:
                input_ = fh.read()
            actual = protocol(input_)
            status = json.loads(actual)['status']
            if status == "OK":
                print("OK")
            else:
                print("FAILED")
                failures = True
        self.assertFalse(failures)

    def test_fail(self):
        success = False
        for f in listdir("tests/failing"):
            print("Testing file {} (should fail)".format(f))
            with open("tests/failing/" + f) as fh:
                input_ = fh.read()
            actual = protocol(input_)
            status = json.loads(actual)['status']
            if status == "OK":
                print("OK (wrong -- test should FAIL!")
                success = True
            else:
                print("FAIL (good -- failure expected)")
        self.assertFalse(success)


if __name__ == '__main__':
    unittest.main()
