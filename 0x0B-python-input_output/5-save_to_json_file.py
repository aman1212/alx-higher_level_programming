#!/usr/bin/python3
"""
Definition of module
"""

def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file, using a JSON representation
    Args
       my_obj - object to be converted to json rep
       filename - file where the json string will be written
    """
    import json
    jsonString = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(jsonString)
        

