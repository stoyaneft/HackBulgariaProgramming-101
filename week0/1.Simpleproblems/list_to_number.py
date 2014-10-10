def list_to_number(digits):
    number = 0
    for i in range(len(digits)):
        digit = digits.pop()
        number += digit * 10 ** i
    return number


def main():
    print(list_to_number([1, 2, 3]))

if __name__ == '__main__':
    main()
