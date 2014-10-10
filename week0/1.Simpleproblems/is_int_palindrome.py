def is_int_palindrome(n):
    num_to_string = str(n)
    reversed_num = ''.join(reversed(num_to_string))
    return reversed_num == num_to_string


def main():
    print(is_int_palindrome(11011))

if __name__ == '__main__':
    main()
