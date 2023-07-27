def no_c(my_string):
    #initialize an empty string
    r = ""
    #loop through each statement in the input string
    for b in my_string:
        #check if the character is not 'c' or 'C'
        if b != ('c') and b != ('C'):
            r +=b
        else:
            r += b
    return r