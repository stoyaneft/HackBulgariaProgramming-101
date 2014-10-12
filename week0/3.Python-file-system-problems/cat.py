import sys

def cat():
    filename = sys.argv[1]
    file = open(filename, 'r')
    content = file.read()
    file.close()
    print(content)

def main():
    cat()

if __name__ == '__main__':
    main()
