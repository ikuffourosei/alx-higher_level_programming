#!/usr/bin/python3


def no_c(my_string):
    new_string = ''
    for chars in my_string:
        if chars == 'c' or chars == 'C':
            pass
        else:
            new_string += chars
    return new_string
