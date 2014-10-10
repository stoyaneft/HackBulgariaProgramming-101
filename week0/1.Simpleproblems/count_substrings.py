def count_substrings(haystack, needle):
    start = 0
    counter = 0
    while start < len(haystack):
        find_position = haystack.find(needle, start)
        if find_position != -1:
            start = find_position + len(needle)
            counter += 1
        else:
            return counter
    return counter


def main():
    print(count_substrings("This is this and that is this", "this"))

if __name__ == '__main__':
    main()
