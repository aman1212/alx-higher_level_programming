#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value = int(value)
        print(value)
    except ValueError:
            return False
    return True
