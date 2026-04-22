# Задача 2: Дано целое число N (>1). Вывести наименьшее из целых чисел K, для которых сумма 1 + 2 + ... + K будет больше или равна N, и саму эту сумму.
N = int(input())
K = 1
current_sum = 1
while current_sum < N:
    K += 1
    current_sum += K
print(K, current_sum)