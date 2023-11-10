#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list and len(my_list):
        x = 0
        y = 0
        for items in my_list:
            x += (items[0] * items[1])
            y += items[1]
        return (x / y)
    return 0
