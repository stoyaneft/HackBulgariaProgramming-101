from number_to_list import number_to_list
from list_to_number import list_to_number


def zero_insert(n):
    digits = number_to_list(n)
    zero_inserted_digits = list(digits)
    counter = 0
    for i in range(len(digits) - 1):
        if digits[i] == digits[i + 1] or (digits[i] + digits[i + 1]) % 10 == 0:
            zero_inserted_digits.insert(i + 1 + counter, 0)
            counter += 1
    return list_to_number(zero_inserted_digits)


def main():
    print(zero_insert(6446464646454543343))

if __name__ == '__main__':
    main()
