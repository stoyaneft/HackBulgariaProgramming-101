def prime_factorization(n):
    factorization = []
    number = n
    for divisor in range(2, n + 1):
        power = 0
        while number % divisor == 0:
            power += 1
            number //= divisor
        if power:
            factorization.append((divisor, power))
    return factorization


def main():
    print(prime_factorization(1000))


if __name__ == '__main__':
    main()
