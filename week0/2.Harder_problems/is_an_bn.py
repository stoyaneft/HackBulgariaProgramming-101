def is_an_bn(word):
    length = len(word)
    return word == 'a' * (length // 2) + 'b' * (length // 2)
