#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        divide = (a / b)
    except ZeroDivisionError:
        divide = None
    finally:
        print("Inside result: {}".format(divde))
    return divide
