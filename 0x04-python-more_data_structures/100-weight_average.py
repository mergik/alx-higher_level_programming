#!/usr/bin/python3
def weight_average(my_list=[]):
    """Returns the weighted average of all ints tuple"""
    if not my_list:
        return 0
    scores = sum(score * weight for score, weight in my_list)
    weights = sum(weight for _, weight in my_list)
    return scores / weights
