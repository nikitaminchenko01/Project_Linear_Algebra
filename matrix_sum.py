def matrix_sum(A, B):
    """    Функция находит сумму двух матриц.

    В качестве аргументов функция принимает две матрицы одиноковой размерности. Создается новая матрица суммы,
    куда записываются элементы, каждый из которых равен сумме соответствующих элементов данных матриц.
    После нахождения всех элементов этой матрицы функция ее возвращает."""
    S = []
    if len(A) == len(B):
        for i in range(len(A)):
            S.append([])
            if len(A[i]) == len(B[i]):
                for j in range(len(A[i])):
                    S[i].append(A[i][j] + B[i][j])
            else:
                raise ValueError('Dimensions of matrices should be equal')
    else:
        raise ValueError('Dimensions of matrices should be equal')
    return S
