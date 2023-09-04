def transpose_matrix(matrix):
    """
    Транспонирование матрицы.

    :param matrix: Исходная матрица в виде списка списков.
    :return: Транспонированная матрица в виде списка списков.
    """
    # Определение числа строк и столбцов в исходной матрице
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Создание пустой матрицы для транспонирования
    transposed = [[0 for _ in range(num_rows)] for _ in range(num_cols)]

    # Заполнение транспонированной матрицы
    for i in range(num_rows):
        for j in range(num_cols):
            transposed[j][i] = matrix[i][j]

    return transposed

# Пример использования функции
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = transpose_matrix(matrix)

# Вывод транспонированной матрицы
for row in transposed_matrix:
    print(row)
