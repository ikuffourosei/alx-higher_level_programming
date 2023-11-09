#!/usr/bin/python3


def common_elements(set_1, set_2):
    new_set = set()
    for items in set_1:
        if items in set_2:
            new_set.add(items)
        else:
            pass
    return new_set
