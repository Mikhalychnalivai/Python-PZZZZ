# В матрице элементы последней строки заменить на 0.

import random

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = [[random.randint(0, 9) for _ in range(cols)] for _ in range(rows)]

print("Исходная матрица:")
for row in matrix:
    print(row)

matrix[-1] = [0 for _ in range(cols)]

print("\nРезультирующая матрица:")
for row in matrix:
    print(row)