def validate_password(password):
    if len(password) < 8:
        return False
    #check for at least an uppercase, lowercase and digit
    its_uppercase = any(char.isuper() for char in password)
    its_lowercase = any(char.islower() for char in password)
    its_digit = any(char.isdigit() for char in password)

    if not (its_uppercase and its_lowercase and its_digit):
        return False
    if ' ' in password:
        return False
    return True