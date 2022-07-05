#!/usr/bin/python3
"""write file"""

def write_file(filename="", text=""):
    """"write file"""
    
    with open(filename, "w", encoding="utf-8") as f:
        data = f.write(text)
        return data
     
