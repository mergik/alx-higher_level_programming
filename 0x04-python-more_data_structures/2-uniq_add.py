#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Returns sum of unique integers in a list"""
    unique = set()
    for num in my_list:
        unique.add(num)
    uniq_sum = sum(unique)
    return uniq_sum
