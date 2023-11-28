def swap_columns(matrix, i, j):
    if 0 <= i < len(matrix[0]) and 0 <= j < len(matrix[0]):
        for row in matrix:
            row[i], row[j] = row[j], row[i]
        return matrix
    else:
        raise ValueError("Некорректные номера столбцов")


try:
    print("Введите размеры матрицы ")
    n = int(input("n: "))
    m = int(input("m: "))
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    print("Введите номера столбцов ")
    i = int(input("i: "))
    j = int(input("j: "))
    result_matrix = swap_columns(matrix, i, j)
    print("Результат обмена столбцов:")
    for row in result_matrix:
        print(*row)
except ValueError as ve:

    print("Ошибка: ", ve)
except Exception as e:
    print("Общая ошибка: ", e)
finally:
    print("До свидания!")
