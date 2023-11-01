#!/usr/bin/python3

def fizzbuzz():
    number = range(1, 101)
    for i in number:
        fizz = i % 3
        buzz = i % 5
        if i < 100:
            if fizz == 0 and buzz != 0:
                print("fizz", end=' ')
            elif buzz == 0 and fizz != 0:
                print("buzz", end=' ')
            elif fizz == 0 and buzz == 0:
                print("fizzbuzz", end=' ')
            else:
                print(i, end=' ')
        else:
            if fizz == 0 and buzz != 0:
                print("fizz", end='')
            elif buzz == 0 and fizz != 0:
                print("buzz", end='')
            elif fizz == 0 and buzz == 0:
                print("fizzbuzz", end='')
            else:
                print(i, end='')
    return i
            
