#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Returns a boolean if integer is printed correctly"""
    try:
        value = int(value)  # Convert value to integer if possible
        print("{:d}".format(value))
        return True
    except ValueError:
        print("Exception: Unknown format code 'd' for object of type '{}'".format(type(value).__name__),
              file=sys.stderr)
    except TypeError:
        print("Exception: '{}' is not an integer".format(value), file=sys.stderr)
    return False
