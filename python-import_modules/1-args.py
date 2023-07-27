#!/usr/bin/python3
import sys

def get_arguments(argv):
    # get number of args passed
    num_arguments = len(argv) - 1
    plural = "s" if num_arguments != 1 else ""

    #printnumber of args
    print("{:d} argument{}{}".format(num_arguments, plural, ":" if num_arguments > 0 else "", end=""))
    #check if there are no args
    if num_arguments == 0:
        print(" 0 arguments.")
    else:
        #print()
    #loop thru and prnt args with their positions
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
#callthe get args with args passed
if __name__ == "__main__":
    get_arguments(sys.argv)