def no_c(my_string):
    #initialize an empty string
    r = ""
    #loop through each statement in the input string
    for b in my_string:
        #check if the character is not 'c' or 'C'
        if b == ('c') or b == ('C'):
            pass
        else:
            r += b
        #elif b.upper() != 'C':
         #   r += b
        #return final result
        return r