# Дана строка, содержащая по крайней мере один символ пробела. Вывести подстроку,
# расположенную между первым и последним пробелом исходной строки. Если
# строка содержит только один пробел, то вывести пустую строку. ПЗ7 - 28 вариант

import tkinter as tk


def solve():
    s = entry.get()

    first_space = s.find(" ")
    last_space = s.rfind(" ")

    if first_space == last_space:
        result = ""
    else:
        result = s[first_space + 1:last_space]

    result_label.config(text=f"Результат: {result}")


root = tk.Tk()
root.title("Задача 2")
root.geometry("500x200")

tk.Label(
    root,
    text="Введите строку:"
).pack(pady=5)

entry = tk.Entry(root, width=60)
entry.pack()

tk.Button(
    root,
    text="Найти подстроку",
    command=solve
).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()