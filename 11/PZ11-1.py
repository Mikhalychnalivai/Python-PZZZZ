from collections import Counter
import random

sequence = [random.randint(1, 10) for _ in range(20)]
print("Исходная последовательность:", sequence)

counts = Counter(sequence)

unique_elements = list(filter(lambda x: counts[x] == 1, sequence))

print("Не повторяющиеся элементы:", unique_elements)
print("Их количество:", len(unique_elements))

modified_sequence = list(map(lambda x: x * 2 if x > 5 else x, sequence))

print("Модифицированная последовательность (>5 умножено на 2):", modified_sequence)