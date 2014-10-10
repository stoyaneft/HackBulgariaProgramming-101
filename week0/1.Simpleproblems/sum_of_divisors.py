def sum_of_divisors(n):
    sum = 1
    for divisor in range(2, n + 1):
        if n % divisor == 0:
            sum += divisor
    return sum


def main():
    print(sum_of_divisors(8))

if __name__ == '__main__':
    main()
