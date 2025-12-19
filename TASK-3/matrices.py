def is_symmetric(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    if rows != cols:
        return False

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[j][i]:
                return False

    return True

def row_sum(matrix):
    sums = []

    for row in matrix:
        sums.append(sum(row))

    return sums

def column_sum(matrix):
    cols = len(matrix[0])
    sums = []

    for j in range(cols):
        col_total = 0
        for i in range(len(matrix)):
            col_total += matrix[i][j]
        sums.append(col_total)

    return sums

def multiply_2x2(mat1, mat2):
    result = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result

def min_max_matrix(matrix):
    min_val = matrix[0][0]
    max_val = matrix[0][0]

    for row in matrix:
        for value in row:
            if value < min_val:
                min_val = value
            if value > max_val:
                max_val = value

    return min_val, max_val
