def contains_digit(number, digit):
    number_to_str = str(number)
    return str(digit) in number_to_str


def main():
    print(contains_digit(1234, 4))

if __name__ == '__main__':
    main()
