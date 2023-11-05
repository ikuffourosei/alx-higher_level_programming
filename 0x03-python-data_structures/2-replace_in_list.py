#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    n = len(my_list)
    if idx >= n or idx < 0:
        my_list
        return my_list
    else:
        my_list.insert(idx, element)          
        return my_list
