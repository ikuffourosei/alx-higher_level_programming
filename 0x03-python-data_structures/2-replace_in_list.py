#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    n = len(my_list)
    if idx >= n or idx < 0:
        return my_list
    else:
        my_list = my_list.insert[element: idx]
        return my_list
