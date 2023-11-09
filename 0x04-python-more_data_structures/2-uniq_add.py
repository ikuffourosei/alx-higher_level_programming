#!/usr/bin/python3


def uniq_add(my_list=[]):
    result = 0
    # to check forr duplicates
    duplicate = []
    for i in my_list:
        if i not in duplicate:
            duplicate.append(i)
            result += i
        else:
            pass
    return result
