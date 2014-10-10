def groupby(func, seq):
    grouped_dict = {}
    for item in seq:
        key = func(item)
        if key not in grouped_dict:
            grouped_dict[key] = [item]
        else:
            grouped_dict[key].append(item)
    return grouped_dict


def main():
    print(groupby(lambda x: 'odd' if x % 2 else 'even',
                  [1, 2, 3, 5, 8, 9, 10, 12]))

if __name__ == '__main__':
    main()
