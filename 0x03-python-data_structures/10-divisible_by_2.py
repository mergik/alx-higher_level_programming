#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list"""
    result_list = []
    for num in my_list:
        result_list.append(num % 2 == 0)
    return result_list
