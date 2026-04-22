# Задача 1: Составить программу, в которой функция генерирует четырехзначное число и определяет, есть ли в числе одинаковые цифры.
import random

def has_duplicate_digits(n):
    s = str(n)
    return len(s) != len(set(s))

num = random.randint(1000, 9999)
print(f"Сгенерированное число: {num}")
if has_duplicate_digits(num):
    print("В числе есть одинаковые цифры")
else:
    print("Все цифры уникальны")