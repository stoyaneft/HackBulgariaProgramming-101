def sevens_in_a_row(arr, n):
    counter = 0
    for number in arr:
        if number == 7:
            counter += 1
        else:
            counter = 0
        if counter == n:
            return True
    return False


def main():
    print(sevens_in_a_row([1, 7, 1, 7, 7], 4))

if __name__ == '__main__':
    main()
