#!/usr/bin/python3
"""
Definition of module
"""

def read_file(filename=""):
    """open and read a file
    Args
       filename
    """
    with open(filename, encoding="utf-8") as f:
        text = f.read()
        print(text, end='')
        

    
    
