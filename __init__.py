from determinant import determinant
from determinant import minorize
from slau_solver import slau
from slau_solver import gauss
from matrix_product import matrix_prod
from matrix_sum import matrix_sum
from function_norm import norm_vector
from function_norm_matrix import norm_matrix
from matrix_invert import matrix_invert

"""Этот пакет представляет собой набор функций для выполнения алгебраических операций с матрицами и векторами.
Функционал пакета:
    determinant - вычисление определителя квадратной матрицы;
    minorize - нахождение минора заданного элемента матрицы;
    slau - решение СЛАУ с произвольной матрицей коэффициентов при неизвестных методом Гаусса;
    gauss - решение СЛАУ с квадратной матрицей коэффициентов при неизвестных методом Гаусса;
    matrix_prod - нахождение произведения двух матриц;
    matrix_sum - нахождение суммы двух матриц;
    norm_vector - вычисление нормы вектора;
    norm_matrix - вычисление нормы матрицы
    matrix_invert - нахождение обратной матрицы"""
