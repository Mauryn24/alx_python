def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        fibo = [0, 1]
        while len(fibo) < n:
            next = fibo[-1] + fibo[-2]
            if next < 0:
                return []
            fibo.append(next)
            return fibo