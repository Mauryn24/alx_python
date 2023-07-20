def is_prime(number):
    if number <= 1:
        return False
    for a in range(2, int(num**0.5) + 1):
        if num % a == 0:
            return False
    return True