#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """Returns a boolean if integer is printed correctly"""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        print("Exception: Invalid value", file=sys.stderr)
        return False
