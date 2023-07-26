def no_c(my_string):
    #initialize an empty string
    r = ""
    #loop through each statement in the input string
    for b in my_string:
        #check if the character is not 'c' or 'C'
        if b.lower() != 'c':
            result += b
        elif b.upper() != 'C':
            result += b
        #return final result
        return r