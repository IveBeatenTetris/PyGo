import json

def loadJSON(path):
    """Load and convert a JSON file."""
    with open(path) as text:
        content = "".join(text.readlines())

    return json.loads(content)
