# Вариант 27
# Задание 1
# Сформировать два текстовых файла с последовательностями целых чисел.
# Создать новый файл со следующими данными:
# - Элементы первого и второго файлов
# - Элементы первого файла, присутствующие во втором
# - Элементы второго файла, присутствующие в первом
# - Количество элементов
# - Количество отрицательных элементов
# - Количество положительных элементов
import os


if not os.path.exists('data1.txt'):
    with open('data1.txt', 'w') as f:
        f.write('-5 3 -8 12 7 -1 4 9 -3 6')

if not os.path.exists('data2.txt'):
    with open('data2.txt', 'w') as f:
        f.write('3 -8 15 -2 7 20 -3 11 4 -6')

with open('data1.txt', 'r') as f:
    list1 = list(map(int, f.read().split()))

with open('data2.txt', 'r') as f:
    list2 = list(map(int, f.read().split()))

combined = list1 + list2

in_both_from1 = [x for x in list1 if x in list2]
in_both_from2 = [x for x in list2 if x in list1]

total_count = len(combined)
neg_count = sum(1 for x in combined if x < 0)
pos_count = sum(1 for x in combined if x > 0)

with open('result27.txt', 'w', encoding='UTF-8') as out:
    out.write(f'Элементы первого и второго файлов: {combined}\n')
    out.write(f'Элементы первого файла, присутствующие во втором: {in_both_from1}\n')
    out.write(f'Элементы второго файла, присутствующие в первом: {in_both_from2}\n')
    out.write(f'Количество элементов: {total_count}\n')
    out.write(f'Количество отрицательных элементов: {neg_count}\n')
    out.write(f'Количество положительных элементов: {pos_count}\n')

print('Задание 1 выполнено. Результат записан в result27.txt')