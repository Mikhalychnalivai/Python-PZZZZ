#В матрице элементы столбца N увеличить в два раза.

import random

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = [[random.randint(0, 9) for _ in range(cols)] for _ in range(rows)]

n = int(input(f"Введите номер столбца от 1 до {cols}: ")) - 1

print("Исходная матрица:")
for row in matrix:
    print(row)

for i in range(rows):
    matrix[i][n] *= 2

print("\nРезультирующая матрица:")
for row in matrix:
    print(row)