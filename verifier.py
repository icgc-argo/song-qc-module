def verify(json):
    if json['name'] == "Hardeep":
        return ['Not Kevin', 'But she would probably write better error messages than this one']
    if json['name'] != "kevin":
        return ['Not Kevin']
    return []
