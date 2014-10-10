def number_to_list(n):
    digits = []
    while n > 0:
        digits.insert(0, n % 10)
        n //= 10
    return digits


def main():
    print(number_to_list(123034))

if __name__ == '__main__':
    main()
