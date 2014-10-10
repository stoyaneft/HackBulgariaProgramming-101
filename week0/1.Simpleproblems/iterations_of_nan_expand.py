from nan_expand import nan_expand


def iterations_of_nan_expand(expanded):
    times_expanded = (len(expanded) - 3) // 6
    nan_expanded = nan_expand(times_expanded)
    if nan_expanded != expanded:
        return False
    return times_expanded


def main():
    print(iterations_of_nan_expand(
        'Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN'))

if __name__ == '__main__':
    main()
