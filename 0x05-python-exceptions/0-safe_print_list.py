#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Returns the number of elements to print"""
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end=" ")
            count += 1
    except IndexError:
        pass
    finally:
        print()
        return count
