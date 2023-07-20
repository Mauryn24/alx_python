def fibonacci_sequence(n):
    #initialize the first two terms of the series
    fibonacci_sequence = [0, 1]
    #generate the rest of the series up to n
    while len(fibonacci_sequence) < n:
        next = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next)
    return fibonacci_sequence