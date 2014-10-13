import sys
from random import randint


def generate_numbers():
    filename = sys.argv[1]
    numbers_count = int(sys.argv[2])
    file = open(filename, 'w')
    rand_numbers = []
    for i in range(numbers_count):
        rand_numbers.append(str(randint(1, 1000)))
    file.write(" ".join(rand_numbers))
    file.close()


def main():
    generate_numbers()

if __name__ == '__main__':
    main()
