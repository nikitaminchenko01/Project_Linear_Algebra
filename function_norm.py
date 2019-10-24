def norm_vector (coordinates):
    """    Функция вычисляет норму вектора.

    В качестве аргумента функция получает список с координатами вектора и находит его норму
    как корень из суммы квадратов координат. Функция возвращает числовое значение нормы."""
    norm = 0
    try:
        for coordinate in coordinates:
            float(coordinate)
            norm += coordinate**2
    except:
        raise ValueError('Incorrect coordinates')
    else:
        return norm**0.5
