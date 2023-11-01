#!/usr/bin/python3
def uppercase(str):
    for alpha in str:
        if 96 < ord(alpha) and ord(alpha) < 123:
            alpha = chr(ord(alpha) - 32)
        print("{:s}".format(alpha), end="")

    print('\n', end="")
