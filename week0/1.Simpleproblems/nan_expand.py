def nan_expand(times):
    if not times:
        return ""
    nota_expand = "Not a " * times
    return nota_expand + "NaN"


def main():
    print(nan_expand(0))

if __name__ == '__main__':
    main()
