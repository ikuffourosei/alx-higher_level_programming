#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())
    for item in sorted_keys:
        value = a_dictionary[item]
        print(f"{item}: {value}")
