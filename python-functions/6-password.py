def validate_password(password):
    #check length of password
    if len(password) < 8:
        return False
    
    #check for at least an uppercase, lowercase and digit
    its_uppercase = False
    its_lowercase = False
    its_digit = False

    for char in password:
        if char.isupper():
            its_uppercase = True
        elif char.islower():
            its_lowercase = True
        elif char.isdigit():
            its_digit = True
    if not (its_uppercase and its_lowercase and its_digit):
        return False
    
    #check if the password contains space
    if ' ' in password:
        return False
    
    #if all checks pass, return True
    return True

""" its_uppercase = any(char.isuper() for char in password)
    its_lowercase = any(char.islower() for char in password)
    its_digit = any(char.isdigit() for char in password)

    if not (its_uppercase and its_lowercase and its_digit):
        return False
    if ' ' in password:
        return False
    return True"""