#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    a = my_list[0]
    for i in my_list:
        if a < i:
            a = i
    return a
