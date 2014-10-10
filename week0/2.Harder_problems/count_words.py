def count_words(arr):
    counted_words = {}
    for word in arr:
        if word not in counted_words:
            counted_words[word] = arr.count(word)
    return counted_words


def main():
    print(count_words(["apple", "banana", "apple", "pie"]))

if __name__ == '__main__':
    main()
