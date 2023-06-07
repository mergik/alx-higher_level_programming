#!/usr/bin/python3

def remove_char_at(string, n):
    """creates a copy of string, removing the char at position n"""
    if n < 0 or n >= len(string):
        return string

    result = ""
    for i in range(len(string)):
        if i != n:
            result += string[i]
    
    return result
