def count_consonants(input_string):
    counter = 0
    CONSONANTS = tuple("bcdfghjklmnpqrstvwxz")
    for letter in input_string:
        if letter.lower() in CONSONANTS:
            counter += 1
    return counter


def main():
    print(count_consonants(
        "Github is the second best thing that" +  
        "happend to programmers, after the keyboard!"))

if __name__ == '__main__':
    main()
