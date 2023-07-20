def is_prime(number):
    if number <= 1:
        return False
    for a in range(2, int(number**0.5) + 1):
        if number % a == 0:
            return False
    return True