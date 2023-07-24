#/usr/bin/python3
def main():
    a = 1
    b = 2

    from add_0 import add
    
    sum = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, sum))

if __name__ == "__main__":
    main()