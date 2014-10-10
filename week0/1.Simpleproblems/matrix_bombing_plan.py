from sum_matrix import sum_matrix


def calculate_damage(x, y, matrix):
    total_damage = 0
    width = len(matrix)
    height = len(matrix[0])
    bomb_value = matrix[x][y]
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                if 0 <= x + i < width and 0 <= y + j < height:
                    if bomb_value < matrix[x + i][y + j]:
                        total_damage += bomb_value
                    else:
                        total_damage += matrix[x + i][y + j]
    return total_damage


def matrix_bombing_plan(m):
    bombing_plan = {}
    TOTAL_VALUE = sum_matrix(m)
    for x in range(len(m)):
        for y in range(len(m[x])):
            position = x, y
            bombing_plan[position] = TOTAL_VALUE - calculate_damage(x, y, m)
    return bombing_plan


def main():
    print(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


if __name__ == '__main__':
    main()
