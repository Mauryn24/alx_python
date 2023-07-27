def best_score(a_dictionary):
    #check if the dictionary is empty
    if not a_dictionary:
        return None
    #initialize variable to store maximum score
    large_score = None
    large_key = None
    #iterate through the key_value
    for key, value in a_dictionary.items():
        #check if current value is greater than current maximum
        if large_score is None or value > large_score:
            #if value is greater than maximum score,
            #update the large score and large key accordingly
            large_score = value
            large_key = key
    #return the key with the biggest value
    return large_key