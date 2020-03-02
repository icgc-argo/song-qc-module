#!/usr/bin/env python3
import unittest

from run import protocol
import json


class UnknownPerson(Exception): pass


def person_verifier(message):
    content = json.loads(message)
    if content['name'] == "Kevin":
        return []
    if content['name'] == "Rob":
        return ['Person is not Kevin']
    if content['name'] == "Alex":
        return "Person is not Kevin"
    if content['name'] == 'Bashar':
        return [{"a": 1, "b": 2}, UnknownPerson('Bashar'), "sadness"]
    else:
        raise UnknownPerson(format(content['name']))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        with open("fixtures/tests.json") as fh:
            test_cases = json.load(fh)

        for t in test_cases['tests']:
            actual, expected, msg = protocol(t['input'], person_verifier), t['expected_output'], t['test_description']
            self.assertEqual(expected, actual, msg=msg)


if __name__ == '__main__':
    unittest.main()
