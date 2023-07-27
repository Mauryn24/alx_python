def common_elements(set_1, set_2):
    b = set(set_1)
    c = set(set_2)

    #check length
    #if len(b.intersection(c)) > 0:
     #   return(b.intersection(c))
    
    #find the common elements using the intersection operation
    common_elements_set = set_1 & set_2
    return common_elements_set