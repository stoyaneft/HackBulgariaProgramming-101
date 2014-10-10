from nth_fib_lists import nth_fib_lists


def member_of_nth_fib_lists(listA, listB, needle):
    if listA == needle or listB == needle:
        return True
    fib_num = 3
    current_fib_list = nth_fib_lists(listA, listB, fib_num)
    while len(current_fib_list) <= len(needle):
        if needle == current_fib_list:
            return True
        fib_num += 1
        current_fib_list = nth_fib_lists(listA, listB, fib_num)
    return False

print(member_of_nth_fib_lists([7, 11], [2], [11, 7, 2, 2, 7]))
