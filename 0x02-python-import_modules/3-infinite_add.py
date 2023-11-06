#!/usr/bin/python3

from sys import argv

# argument count
argv_count = (len(argv) - 1)
result = 0

# if no arguments are passed
if argv_count == 0:
    print("{:d}".format(argv_count))

# if an argument or more is passed
else:
    for num in range(1, argv_count + 1):
        result += int(argv[num])
    print("{:d}".format(result))
