#!/usr/bin/python3
def print_last_digit(number):
    if number != 0:
        if number > 0:
            last_digit = number % 10
            print(f"{last_digit}", end='')
        elif number < 0:
            last_digit = (abs(number) % 10)
            print(f"{last_digit}", end='')
    else:
        last_digit = 0
        print(f"{last_digit}", end='')
    return last_digit
