#!/usr/bin/python3
"""
Definition of module
"""

def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdou"""
    with open(filename, encoding="utf-8") as f:
        print(f.read())
        

        

    
    
