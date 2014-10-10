def sum_matrix(m):
    return sum(map(sum, m))


def main():
    print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))

if __name__ == '__main__':
    main()
