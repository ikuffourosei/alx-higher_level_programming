#!/usr/bin/python3
for num1 in range(10):
    for num2 in range(num1 + 1, 10):
        if num1 <= 7:
            print('{}{}'.format(num1, num2), end=", ")
        else:
            print('{}{}'.format(num1, num2))
