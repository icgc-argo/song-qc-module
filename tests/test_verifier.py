#!/usr/bin/env python3
import unittest
from os import listdir
from run import protocol

import json


class MyTestCase(unittest.TestCase):
    def test_success(self):
        for f in listdir("passing"):
            with open(f) as fh:
                input = fh.read()
            actual = protocol(input)
            status = json.loads(actual)['status']
            assert status == "OK"

    def test_fail(self):
        for f in listdir("failing"):
            with open(f) as fh:
                input = fh.read()
            actual = protocol(input)
            status = json.loads(actual)['status']
            assert status != "OK"


if __name__ == '__main__':
    unittest.main()
