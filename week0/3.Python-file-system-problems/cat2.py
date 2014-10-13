import sys


def cat2():
    for i, filename in enumerate(sys.argv[1:]):
        file = open(filename, 'r')
        content = file.read()
        print(content)
        if i != len(sys.argv) - 1:
            print()
        file.close()
    print(content)


def main():
    cat2()

if __name__ == '__main__':
    main()
