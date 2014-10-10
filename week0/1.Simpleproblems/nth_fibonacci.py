def nth_fibonacci(n):
    if n <= 2:
        return 1
    else:
        last = 1
        previous = 1
        for i in range(2, n):
            next = last + previous
            previous = last
            last = next
        return last


def main():
    print(nth_fibonacci(10))

if __name__ == '__main__':
    main()
