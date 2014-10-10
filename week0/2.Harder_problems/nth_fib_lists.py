def nth_fib_lists(listA, listB, n):
    if n == 1:
        return listA
    elif n == 2:
        return listB
    else:
        last = list(listB)
        previous = list(listA)
        for i in range(2, n):
            next = list(previous)
            next.extend(last)
            previous = list(last)
            last = list(next)
    return last


def main():
    print(nth_fib_lists([1, 2], [3], 5))


if __name__ == '__main__':
    main()
