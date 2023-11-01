#!/usr/bin/python3

def fizzbuzz():
    number = range(1, 101)
    for i in number:
        fizz = i % 3
        buzz = i % 5
        if fizz == 0 and buzz != 0:
            print("Fizz", end=' ')
        elif buzz == 0 and fizz != 0:
            print("Buzz", end=' ')
        elif fizz == 0 and buzz == 0:
            print("FizzBuzz", end=' ')
        else:
            print(i, end=' ')
    return i
