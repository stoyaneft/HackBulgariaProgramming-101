from is_prime import is_prime


def prime_number_of_divisors(n):
    number_of_divisors = 1
    for divisor in range(2, n + 1):
        if n % divisor == 0:
            number_of_divisors += 1
    return is_prime(number_of_divisors)


def main():
    print(prime_number_of_divisors(9))

if __name__ == '__main__':
    main()
