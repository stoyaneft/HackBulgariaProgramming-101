import sys
import re


def wc():
    command = sys.argv[1]
    filename = sys.argv[2]
    file = open(filename, 'r')
    content = file.read()
    if command == 'chars':
        print(len(content))
    elif command == 'words':
        words = re.findall('\w+', content)
        print(len(words))
    elif command == 'lines':
        lines = content.split('\n')
        print(len(lines))
    file.close()


def main():
    wc()


if __name__ == '__main__':
    main()
