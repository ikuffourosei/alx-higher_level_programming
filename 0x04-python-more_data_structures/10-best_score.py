#!/usr/bin/python3


def best_score(a_dictionary):
    # Handle cases of empty dictionary
    if not a_dictionary:
        return None
    # get listof values and find max
    maxx = max(a_dictionary.values())
    for key,val in a_dictionary.items():
        if val == maxx:
            return key
    return None
