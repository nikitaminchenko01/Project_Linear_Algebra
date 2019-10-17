import copy


def minorize(matrix, row, column):
    try:
        minor = copy.deepcopy(matrix)
        [minor[i].pop(column) for i in range(len(minor))]
        minor.pop(row)
        return minor
    except:
        raise ValueError('Incorrect elements of matrix')


def determinant(matrix):
    try:
        if len(matrix) != len(matrix[0]):
            raise ValueError('Incorrect dimensions')
        det = 0
        if len(list(matrix)) == 1:
            return matrix[0][0]
        for j in range(len(matrix[0])):
            det += (-1)**j * matrix[0][j] * determinant(minorize(matrix, 0, j))
        return det
    except:
        raise ValueError('Incorrect elements of matrix')
