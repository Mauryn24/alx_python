def update_dictionary(a_dictionary, key, value):
    #if key exists, replace its value with new value
    if key  in a_dictionary:
        a_dictionary[key] = value
    else:
        #if it does not exist, add new values
        a_dictionary[key] = value
    return a_dictionary