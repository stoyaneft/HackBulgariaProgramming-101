def evaluate_fraction(fraction):
    return float(fraction[0]) / fraction[1]


def sort_fractions(fractions):
    print(sorted(fractions, key=evaluate_fraction))


def main():
    print(
        sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))


if __name__ == '__main__':
    main()
