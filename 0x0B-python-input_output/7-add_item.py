#!/usr/bin/python3
"""Module that loads, adds and saves arguments to a Python list"""
import sys


save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    # Add arguments to the list
    arguments = sys.argv[1:]

    # Load existing items from file
    try:
        existing_items = load_file("add_item.json")
    except FileNotFoundError:
        existing_items = []

    # Add new arguments to the list
    existing_items.extend(arguments)

    # Save the updated list to the file
    save_file(existing_items, "add_item.json")
