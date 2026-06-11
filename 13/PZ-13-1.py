#В исходном текстовом файле (dates.txt) найти все даты в форматах ДД.ММ.ГГГГ и ДД/ММ/ГГГГ. Посчитать количество дат в каждом формате.
#Поместить в новый текстовый файл все даты февраля в формате ДД/ММ/ГГГГ.

import re

with open("dates.txt", "r", encoding="utf-8") as file:
    text = file.read()

dates_dot = re.findall(r"\b\d{2}\.\d{2}\.\d{4}\b", text)
dates_slash = re.findall(r"\b\d{2}/\d{2}/\d{4}\b", text)

print("Даты формата ДД.ММ.ГГГГ:")
for date in dates_dot:
    print(date)
print("\nКоличество:", len(dates_dot))

print("\nДаты формата ДД/ММ/ГГГГ:")
for date in dates_slash:
    print(date)
print("\nКоличество:", len(dates_slash))

february_dates_dot = re.findall(r"\b\d{2}\.02\.\d{4}\b", text)
february_dates_slash = re.findall(r"\b\d{2}/02/\d{4}\b", text)
february_dates = [date.replace(".", "/") for date in february_dates_dot] + february_dates_slash

with open("february_dates.txt", "w", encoding="utf-8") as file:
    for date in february_dates:
        file.write(date + "\n")

print("\nДаты февраля в формате ДД/ММ/ГГГГ:")
for date in february_dates:
    print(date)
print("\nКоличество:", len(february_dates))

