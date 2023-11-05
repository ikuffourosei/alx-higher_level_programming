#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    n = len(my_list)
    new_list = []
    if idx >= n or idx < 0:
        return my_list
    else:
        for i in range(n):
            if i == idx:
                new_list.append(element)
            else:
                new_list.append(my_list[i])
        return new_list
