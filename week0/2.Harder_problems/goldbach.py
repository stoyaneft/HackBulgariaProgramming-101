def is_prime(n):
    n = abs(n)
    if n == 1:
        return False
    else:
        for divisor in range(2, int(n ** 0.5) + 1):
            if n % divisor == 0:
                return False
        return True


def goldbach(n):
    prime_numbers = list(filter(is_prime, range(2, int(n // 2 + 1))))
    gb_conjecture = [(prime, n-prime)
                     for prime in prime_numbers if is_prime(n - prime)]
    return gb_conjecture
