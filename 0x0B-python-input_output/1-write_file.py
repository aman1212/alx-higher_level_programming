#!/usr/bin/python3
"""
Definition of module
"""

def write_file(filename="", text=""):
    """writes a string to a text file and returns the number of characters written
    Args
       filename - file name
       text - string to be written
    """
    with open(filename, "w", encoding="utf-8") as f:
        data = f.write(text)
        return data
     
