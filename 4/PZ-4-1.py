# Задача 1: Дано целое число N (>0). Найти сумму 1 + 1/2 + 1/3 + ... + 1/N
N = int(input())
total = sum(1/i for i in range(1, N+1))
print(total)