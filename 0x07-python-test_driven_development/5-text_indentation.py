#!/usr/bin/python3
"""
This module provides a function for indenting text.
"""


def text_indentation(text):
    """
    Indents a given text by adding 2 new lines after each of the characters
    '.', '?', and ':'.

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If `text` is not a string.
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Remove leading and trailing whitespace from the text
    text = text.strip()

    # Iterate through each character in the text
    output = ""
    for char in text:
        # Add the character to the output
        output += char

        # Check if the character is ., ?, or :
        if char in [".", "?", ":"]:
            # Add two newlines after the character
            output += "\n\n"

    # Print the resulting indented text
    print(output)
