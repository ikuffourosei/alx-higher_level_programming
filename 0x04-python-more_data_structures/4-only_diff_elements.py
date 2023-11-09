#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    # initialize an empty set
    unique_set = set()
    for items in set_1:
        if items not in set_2:
            unique_set.add(items)
    for items in set_2:
        if items not in set_1:
            unique_set.add(items)
    return unique_set
