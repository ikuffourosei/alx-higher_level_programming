#!/usr/bin/python3

import sys

# argument count
argv_count = (len(sys.argv) - 1)
result = 0

# if no arguments are passed
if argv_count == 0:
    print(f"{argv_count}")

# if an argument or more is passed
else:
    for num in range(1, argv_count + 1):
        result += int(sys.argv[num])
    print(result)
