def is_increasing(seq):
    for i in range(len(seq) - 1):
        if seq[i] >= seq[i + 1]:
            return False
    return True


def main():
    print(is_increasing([1, 3, 4, 2]))

if __name__ == '__main__':
    main()
