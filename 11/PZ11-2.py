def to_lower_generator(s):
    for char in s:
        yield char.lower()

text = "ПриВЕТ! Как ДЕлА?"
result = ''.join(to_lower_generator(text))
print("Результат:", result)