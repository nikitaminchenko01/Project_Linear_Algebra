def norm_matrix(elements):
    """    Функция вычисляет M-норму матрицы.

    В качестве аргумента функция получает матрицу в виде списка списков и находит её M-норму,
    т.е. максимальную сумму элементов строки матрицы. Функция возвращает числовое значение нормы."""
    norm = 0
    sum_row = []
    try:
        for row in elements:
            sum = 0
            for element in row:
                float(element)
                sum += element
            sum_row.append(sum)
        norm = max(sum_row)
    except:
        raise ValueError('Incorrect elements')
    else:
        return norm

