#!/usr/bin/python3
import sys


def print_arguments(*argv):
    """prints the number of and the list of its arguments"""
    # count how many args were passed in,
    #  starting from 1 (not including script name)
    i = 0
    length = len(sys.argv) - 1
    if length == 1:
        print("{:d} argument:".format(length))
    elif length == 0:
        print("{:d} arguments.".format(length))
    else:
        print("{:d} arguments:".format(length))
    # loop through all the system arguments passed
    for args in sys.argv:
        if i != 0:
            print("{}: {}".format(i, args))
        i += 1


if __name__ == "__main__":
    print_arguments()