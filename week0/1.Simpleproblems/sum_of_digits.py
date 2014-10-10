def sum_of_digits(n):
    _sum = 0
    n = abs(n)
    while n != 0:
        _sum += n % 10
        n //= 10
    return _sum


def main():
    print(sum_of_digits(-10))

if __name__ == '__main__':
    main()
