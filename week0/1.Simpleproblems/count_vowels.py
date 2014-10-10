def count_vowels(intput_string):
    VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
    counter = 0
    for letter in intput_string:
        if letter.lower() in VOWELS:
            counter += 1
    return counter


def main():
    print(count_vowels(
        "Github is the second best thing that happend to programmers, after the keyboard!"))

if __name__ == '__main__':
    main()
