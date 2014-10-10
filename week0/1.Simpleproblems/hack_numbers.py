def to_binary(number):
    binary_number = []
    while number:
        binary_number.append(str(number % 2))
        number //= 2
    return ''.join(reversed(binary_number))


def is_str_palindrome(input_string):
    return input_string == ''.join(reversed(input_string))


def are_units_prime(binary_number):
    count = binary_number.count('1')
    return count % 2 == 1


def next_hack(number):
    while True:
        number += 1
        binary_number = to_binary(number)
        if is_str_palindrome(binary_number) and are_units_prime(binary_number):
            return number


def main():
    print(next_hack(8031))

if __name__ == '__main__':
    main()
