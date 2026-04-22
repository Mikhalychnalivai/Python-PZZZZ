#Дано множество A из N точек (N > 2, точки заданы своими координатами x, y). Найти наименьший периметр треугольника, вершины которого 
#принадлежат различным точкам множества A, и сами эти точки (точки выводятся в том же порядке, в котором они перечислены при 
#задании множества A). Расстояние R между точками с координатами (x1, y1) и (x2, y2) вычисляется по 
#формуле: R = √((x2 - x1)² + (y2 - y1)²). Для хранения 
#данных о каждом наборе точек следует использовать по два списка: первый список для хранения абсцисс, второй — для хранения ординат.

N = int(input("Введите количество точек N (> 2): "))

x_coords = []
y_coords = []

for i in range(N):
    x = float(input(f"Введите x координату точки {i+1}: "))
    y = float(input(f"Введите y координату точки {i+1}: "))
    x_coords.append(x)
    y_coords.append(y)

def distance(i, j):
    dx = x_coords[i] - x_coords[j]
    dy = y_coords[i] - y_coords[j]
    return (dx*dx + dy*dy) ** 0.5

min_perimeter = float('inf')
best_i, best_j, best_k = -1, -1, -1

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            a = distance(i, j)
            b = distance(j, k)
            c = distance(k, i)
            perimeter = a + b + c

            if perimeter < min_perimeter:
                min_perimeter = perimeter
                best_i, best_j, best_k = i, j, k

print(f"\nНаименьший периметр треугольника: {min_perimeter:.6f}")
print("Точки, образующие этот треугольник (в порядке их ввода):")
print(f"Точка {best_i + 1}: ({x_coords[best_i]}, {y_coords[best_i]})")
print(f"Точка {best_j + 1}: ({x_coords[best_j]}, {y_coords[best_j]})")
print(f"Точка {best_k + 1}: ({x_coords[best_k]}, {y_coords[best_k]})")