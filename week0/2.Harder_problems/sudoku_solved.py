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
