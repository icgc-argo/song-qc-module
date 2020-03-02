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
    test_cases = [("<json><name>Kevin</name></json>", '{"status": "ISSUES", "details": ["BAD JSON: Expecting value: line 1 '
                                                      'column 1 (char 0)"]}', "Invalid Json"),
                  ('{"name": "Kevin"}', '{"status": "OK", "details": []}', "Valid -- No errors"),
                  ('{"name": "Rob"}', '{"status": "ISSUES", "details": [\"Person is not Kevin\"]}', "Valid -- errors"),
                  ('{"name": "Alex"}', '{"status": "VERIFIER_ERROR", '
                                       '"details": ["Verifier must return a list of strings, not a <class \'str\'>"]}',
                   "Verifier doesn't return list"),
                  ('{"name": "Bashar"}',
                   '{"status": "VERIFIER_ERROR", '
                   '"details": ["Non string object in list -- element 0 has type <class \'dict\'> instead."]}',
                   "list contains non-strings"),
                  ('{"name": "Rosi"}',
                   '{"status": "VERIFIER_ERROR", "details": ["Verifier exception: UnknownPerson(\'Rosi\')"]}',
                   "Verifier throws exception")]

    def test_something(self):
        for t in self.test_cases:
            if len(t) != 3:
                pass
            actual, expected, msg = protocol(t[0], person_verifier), t[1], t[2]
            self.assertEqual(expected, actual, msg=msg)


if __name__ == '__main__':
    unittest.main()
