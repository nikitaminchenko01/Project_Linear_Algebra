def matrix_prod(A, B):
    if len(A[0]) == len(B):
        result = []
        for i in range(len(A)):
            row =[]
            for j in range(len(B[i])):
                element = 0
                for k in range(len(B)):
                    element += A[i][k] * B[k][j]
                row.append(element)
            result.append(row)
        return result
    else:
        raise ValueError('Incorrect dimensions')

