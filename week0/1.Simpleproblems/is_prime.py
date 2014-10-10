def is_prime(n):
    n = abs(n)
    if n == 1:
        return False
    else:
        for divisor in range(2, n ** 0.5 + 1):
            if n % divisor == 0:
                return False
        return True


def main():
    print(is_prime(-10))

if __name__ == '__main__':
    main()
