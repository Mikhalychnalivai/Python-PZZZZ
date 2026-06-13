# Составить генератор (yield), который переведет символы строки из верхнего
# регистра в нижний.
def to_lower_generator(s):
    for char in s:
        yield char.lower()

text = "ПриВЕТ! Как ДЕлА?"
result = ''.join(to_lower_generator(text))
print("Результат:", result)