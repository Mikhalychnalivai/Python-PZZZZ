# Задание 2
# Из текстового файла (text18-27.txt) вывести содержимое и количество пробельных символов.
# Сформировать новый файл, поставив последнюю строку фразой, введённой пользователем.

for enc in ('utf-16', 'utf-8', 'cp1251'):
    try:
        with open('text18-27.txt', 'r', encoding=enc) as f:
            lines = f.readlines()
        break
    except (UnicodeDecodeError, UnicodeError):
        continue

print('Содержимое файла text18-27.txt:')
for line in lines:
    print(line, end='')

space_count = sum(1 for line in lines for ch in line if ch.isspace())
print(f'\nКоличество пробельных символов: {space_count}')

user_phrase = input('\nВведите фразу для замены последней строки: ')

new_lines = lines[:-1] + [user_phrase + '\n']

with open('text18-27_new.txt', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print('Задание 2 выполнено. Результат записан в text18-27_new.txt')
