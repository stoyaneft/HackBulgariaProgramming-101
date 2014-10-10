from contains_digit import contains_digit


def contains_digits(number, digits):
    for digit in digits:
        if not contains_digit(number, digit):
            return False
    return True


def main():
    print(contains_digits(1234, [4, 2, 5]))

if __name__ == '__main__':
    main()
