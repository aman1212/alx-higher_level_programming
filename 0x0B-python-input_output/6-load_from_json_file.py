#!/usr/bin/python3
"""
Definition of module
"""

def load_from_json_file(filename):
    """function that creates an Object from a JSON file
    Args
      filename - file where the json string located
    """
    import json
    with open(filename, encoding="utf-8") as f:
        jsonString = f.read()
        return json.loads(jsonString)
    
    
        

