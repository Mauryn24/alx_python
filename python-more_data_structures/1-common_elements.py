def common_elements(set_1, set_2):
    b = set(set_1)
    c = set(set_2)

    #check length
    if len(b.intersection(c)) > 0:
        return(b.intersection(c))
    
    #if (b & c):
     #   print(b & c)