#/usr/bin/python3
"""In Python, if __name__ == "__main__": is a commonly used construct that allows you to determine whether a Python script is being run as the main program or if it's being imported as a module into another script"""
if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))