def magic_square(matrix):
    row_sums = list(map(sum, matrix))
    if len(set(row_sums)) != 1:
        return False
    square_size = len(matrix)
    columns = []
    forward_diagonal = []
    backward_diagonal = []
    for i in range(square_size):
        columns.append([row[i] for row in matrix])
        forward_diagonal.append(matrix[i][i])
        backward_diagonal.append(matrix[square_size - 1 - i][i])
    col_sums = list(map(sum, columns))
    if row_sums != col_sums:
        return False
    forw_diag_sum = sum(forward_diagonal)
    back_diag_sum = sum(backward_diagonal)
    return forw_diag_sum == back_diag_sum and forw_diag_sum == row_sums[0]

print(magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))
