#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists"""
    new_list = []
    try:
        for i in range(list_length):
            try:
                num1 = my_list_1[i]
                num2 = my_list_2[i]
                result = num1 / num2
                new_list.append(result)
            except ZeroDivisionError:
                new_list.append(0)
                print("division by 0")
            except (TypeError, ValueError):
                new_list.append(0)
                print("wrong type")
            except IndexError:
                new_list.append(0)
                print("out of range")
    finally:
        return new_list
