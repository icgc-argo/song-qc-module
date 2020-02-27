import json

# fictional example verifier
def verify(message):
    j = json.loads(message)
    if j['name'] == "Hardeep":
        return ['Not Kevin', 'But she would probably write better error messages than this one']
    if j['name'] != "kevin":
        return ['Not Kevin']
    return []
