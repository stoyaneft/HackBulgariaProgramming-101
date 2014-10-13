import sys


def sum_numbers():
    filename = sys.argv[1]
    file = open(filename, 'r')
    numbers = file.read()
    numbers = numbers.split(" ")
    numbers = list(map(int, numbers))
    print(sum(numbers))


def main():
    sum_numbers()

if __name__ == '__main__':
    main()
