import Project_Linear_Algebra as linalg


A1 = [[2, 1, -1, 1], [3, 1, 2, -3], [5, 1, -1, 2], [2, -1, 1, -3]]
A2 = [[0, 3, 1], [3, 3, 3], [4, 10, 5], [9, 3, 3]]
B1 = [1, 2, -1, 4]
B2 = [0, 3, 0, 9]
A3 = [[1, -2, 1, -1, 1], [2, 1, -1, 2, -3], [3, -2, -1, 1, -2], [2, -5, 1, -2, 2]]
A4 = [[2, 1, -1, 1, 12], [3, 1, 2, -3, -1], [5, 1, -1, 2, 2], [2, -1, 1, -3, 0]]
B3 = [0, 0, 0, 0]
print('Обратная матрица:', linalg.matrix_invert(A1))
print('Произведение матриц:', linalg.matrix_prod(A1, A2))
print('Определитель матрицы равен:', linalg.determinant(A1))
print('Норма вектора равна:', linalg.norm_vector(B1))
print('Норма матрицы равна:', linalg.norm_matrix(A1))
print('Сумма матриц равна: ', linalg.matrix_sum(A4, A3))
print('Решение СЛАУ:', linalg.slau(A1, B1))
#print('Решение СЛАУ:', linalg.slau(A2, B2))
#print('Решение СЛАУ:', linalg.slau(A3, B3))
