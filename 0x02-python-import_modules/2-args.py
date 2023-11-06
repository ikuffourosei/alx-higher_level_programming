#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    # length of arguments
    argv_count = (len(sys.argv) - 1)

    # if no argument was passed
    if argv_count == 0:
        print("{:d} arguments.".format(argv_count))
    # if exactly one argument was passed
    elif argv_count == 1:
        print(f"{:d} argument:".format(argv_count))
        for num in range(1, argv_count + 1):
            print("{}: {]".format(num, sys.argv[num]))

        # if arguments are more than 1
    else:
        print(f"{argv_count} arguments:")
        for num in range(1, argv_count + 1):
            print("{}: {}".format(num, sys.argv[num]))
