#!/usr/bin/python3
"""
Definition of module
"""

def to_json_string(my_obj):
    """returns the JSON representation of an object
    Args
       my_obj - object to be converted to json rep
    """
    import json
    return json.dumps(my_obj)
