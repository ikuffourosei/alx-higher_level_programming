#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    # get the keys and value of the dictionary as a list
    values_list = a_dictionary.items()
    change = lambda item: (item[0], item[1] * 2)
    new_dict = dict(map(change, values_list))
    return new_dict
