# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint
n1 = -100
m1 = 100
# Создаем матрицу размерности m x n
n = 10
m = 10
A = [[0 for i in range(m)] for j in range(n)]
#print(A)

# Заполняем матрицу случайными числами
for i in range(n):
    for j in range(m):
        A[i][j] = randint(n1, m1)
#print(A)

# Найдем минимальные элементы в каждом столбце матрицы
c = []
x = m1 + 1
for i in range(len(A)):
    for j in range(m):
        if x > A[i][j]:
            x = A[i][j]
    c.append(x)
    x = m1 + 1
#print(c)
# Найдем максимальное среди этих минимальных чисел
y = n1 - 1
for i in c:
    if y < i:
        y = i
print('Это число:', y)