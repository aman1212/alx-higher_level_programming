#!/usr/bin/python3
"""
Definition of module
"""

def append_write(filename="", text=""):
    """appends a string at the end of a text file and returns the number of characters written
    Args
       filename - file name
       text - string to be written
    """
    with open(filename, "a", encoding="utf-8") as f:
        data = f.write(text)
        return data
    
