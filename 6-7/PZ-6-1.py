#Дан список A размера N. Найти максимальный элемент из его элементов с нечетными номерами: A₁, A₃, A₅, ...
N = int(input("Введите размер списка N: "))
A = []
for i in range(N):
    A.append(int(input(f"Введите элемент A[{i+1}]: ")))

odd_indexed_elements = A[::2]

max_odd = max(odd_indexed_elements)

print(f"Максимальный элемент среди элементов с нечётными номерами: {max_odd}")