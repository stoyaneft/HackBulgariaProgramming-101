def is_solved(row):
    return len(set(row)) == 9


def element_solved(element):
    return all(map(is_solved, element))


def sudoku_solved(sudoku):
    if not element_solved(sudoku):
        return False
    columns = []
    for i in range(9):
        columns.append([row[i] for row in sudoku])
    if not element_solved(columns):
        return False
    subgrids = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            for k in range(0, 2):
                subgrids.extend(sudoku[j + k][i: i + 3])
    return is_solved(subgrids)


print(sudoku_solved([
    [4, 5, 2, 3, 8, 9, 7, 1, 6],
    [3, 8, 7, 4, 6, 1, 2, 9, 5],
    [6, 1, 9, 2, 5, 7, 3, 4, 8],
    [9, 3, 5, 1, 2, 6, 8, 7, 4],
    [7, 6, 4, 9, 3, 8, 5, 2, 1],
    [1, 2, 8, 5, 7, 4, 6, 3, 9],
    [5, 7, 1, 8, 9, 2, 4, 6, 3],
    [8, 9, 6, 7, 4, 3, 1, 5, 2],
    [2, 4, 3, 6, 1, 5, 9, 8, 7]
]))
