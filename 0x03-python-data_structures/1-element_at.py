#!/usr/bin/python3

def element_at(my_list, idx):
    n = len(my_list)
    result = my_list[idx]
    if idx >= n or idx < 0:
        return None
    else:
        return result
