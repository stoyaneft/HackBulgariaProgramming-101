import sys
import os


def concat_files():
    filenames = sys.argv[1:]
    MEGATRON = open('MEGATRON.txt', 'a')
    if os.stat("MEGATRON.txt").st_size != 0:
        MEGATRON.write('\n')
    for i, filename in enumerate(filenames):
        file = open(filename, 'r')
        content = file.read()
        MEGATRON.write(content)
        if i != len(filenames) - 1:
            MEGATRON.write('\n')
        file.close()


def main():
    concat_files()


if __name__ == '__main__':
    main()
