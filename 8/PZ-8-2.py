#сгенерировать словарь от 0 до 6, удалить в нем первый и последний элемент и показать исходный словарь приминяя for, range
cubes = {}

for i in range(7):
    cubes[i] = i ** 3

print("Исходный словарь:", cubes)

del cubes[0]

last_key = max(cubes)
del cubes[last_key]

print("После удаления первого и последнего:", cubes)