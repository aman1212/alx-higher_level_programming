#!/usr/bin/python3
"""
Definition of module
"""

def from_json_string(my_str):
    """returns an object represented by a JSON string
    Args
       my_str - JSON string
    """
    import json
    return json.loads(my_str)

