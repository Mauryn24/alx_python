#!/usr/bin/python3
import sys

if __name__ == "__main__":
    def get_arguements(argv):
        # get number of args passed
        num_arguements = len(argv) -1

        plural = "s" if num_arguements != 1 else ""

        #printnumber of args
        print("{:d} arguement{}".format(num_arguements, plural))

        if num_arguements == 0:
            print(" .")
        else:
            print()
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
        get_arguements(sys.argv)