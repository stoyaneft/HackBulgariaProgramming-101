def is_number_balanced(n):
    digits = []
    while n != 0:
        digits.append(n % 10)
        n //= 10
    count_of_digits = len(digits)
    first_half = digits[:count_of_digits // 2]
    if count_of_digits % 2 == 1:
        second_half = digits[(count_of_digits // 2 + 1):]
    else:
        second_half = digits[count_of_digits // 2:]
    return sum(first_half) == sum(second_half)


def main():
    print(is_number_balanced(1238033))

if __name__ == '__main__':
    main()
