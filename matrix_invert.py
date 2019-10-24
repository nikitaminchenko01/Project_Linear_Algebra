from determinant import determinant
from determinant import minorize


def matmin(matrix):
    """    Функция определяет матрицу миноров.

    Функция принимает в качестве аргумента квадратную матрицу. Для каждого элемента
    матрицы функция считает его миноры путем вызова функции minorize,
    тем самым вычеркивая строку и стобец, в котором стоит элемент, а затем от этой функции
    вызывается функция determinant, которая считает определитель полученного выражения.
    Таким образом, получается матрица миноров."""
    try:
        ma = []
        for i in range(len(matrix)):
            ma.append([])
            for j in range(len(matrix)):
                ma[i].append(0)

        if len(matrix) == 1:
            return matrix[0][0]

        for i in range(len(matrix[0])):
            for j in range(len(matrix[0])):
               ma[i][j] = determinant(minorize(matrix,i,j))



        return ma
    except:
        raise ValueError('Incorrect dimensions')


def matrix_invert(matrix):
    """    Функция считает обратную матрицу.

    Функция принимает в качестве аргумента матрицу в виде списка списков, вызовом функции
    matmin получает матрицу миноров. Затем транспонирует ее, одновременно считая каждый элемент,
    умноженный на обратный определитель."""
    degenerate = False
    try:
        if determinant(matrix)!=0:
            trans = []
            M = matmin(matrix)
            for j in range(len(M[0])):
                t = []
                for i in range(len(M)):
                    if (i+j) % 2 != 0:
                        t = t + [-M[i][j]/determinant(matrix)]
                    else:
                        t = t + [M[i][j]/determinant(matrix)]

                trans = trans + [t]
            return trans
        else:
            degenerate = True
    except:
        raise ValueError('Incorrect dimensions')
    else:
        if degenerate:
            raise ValueError('Matrix cannot be inverted as it is degenerate')
