import copy


def minorize(matrix, row, column):
    """    Функция находит минор элемента матрицы.

    Функция принимает в качестве аргументов матрицу, представленную в виде списка списков,
    минор которой нужно найти, номер строки и номер столбца элемента, к которому нужно
    найти минор. Создается копия матрицы и из нее удаляются строка и столбец с указанными номерами."""
    try:
        minor = copy.deepcopy(matrix)
        [minor[i].pop(column) for i in range(len(minor))]
        minor.pop(row)
        return minor
    except:
        raise ValueError('Incorrect elements of matrix')


def determinant(matrix):
    """    Функция считает числовое значение определителя квадратной матрицы.

    Функция принимает в качестве аргумената квадратную матрицу, представленную в виде
    списка списков и вычисляет значение её определителя методом алгебраических
    дополнений. Для этого находится сумма всех произведений элементов первого столбца
    определителя на их алгебраические дополнения. Миноры, соответствующие этим
    алгебраическим дополнениям, находит вызываемая функция minorize(), а их числовые
    значения вычисляются рекурсивно.
    В случае, если матрица не является квадратной и/или её элементы не являются
    числами, возвращается ошибка.
    В противном случае функция возвращает числовое значение определителя."""
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

        

def matalgcompl(matrix):
        """    Функция считает транспонированную матрицу алгебраических дополнений.

    Функция принимает в качестве аргумента квадратную матрицу. Для каждого элемента 
    матрицы функция считает его алгебраическое дополнения путем вызова функции minorize,
    тем самым вычеркивая строку и стобец, в котором стоит элемент, а затем от этой функции 
    вызывается функция determinant, которая считает определитель полученного выражения. Таким
    образом, получается матрица алгебраических дополнений."""
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
        raise ValueError('Incorrect')



def transposealgcompl(matrix):
        """    Функция считает обратную матрицу.

    Функция принимает в качестве аргументов матрицу алгебраических дополнений. Затем 
    транспонирует ее, одновременно считая каждый элемент, умноженный на обратный определитель.
    """
    try:
        if determinant(matrix)!=0:
            trans = []
            for j in range(len(matalgcompl(matrix)[0])):
                t = []
                for i in range(len(matalgcompl(matrix))):
                    if (i+j)%2!=0:
                        t = t + [-matalgcompl(matrix)[i][j]/determinant(matrix)]
                    else:
                        t = t + [matalgcompl(matrix)[i][j]/determinant(matrix)]

                trans = trans  + [t]
            return trans
        else:
            print('Matrix is degenerate')
    except:
        raise ValueError('Incorrect')







