"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint

a = [0 for i in range(20)]
for i in range(len(a)):
    a[i] = randint(0, 20)

print(a)
# Найдем максимальное и минимальное значение и их индексы
x = 0
y = 100
xi = 0
yi = 0
for i in range(len(a)):
    if x < a[i]:
        x = a[i]
        xi = i
    if y > a[i]:
        y = a[i]
        yi = i
print(xi, yi)
#Найдем сумму элементов, находящихся между максимальным и минимальным значениями
b = 0
if xi < yi:
    for i in range(xi+1, yi):
        b += a[i]
else:
    for i in range(xi-1, yi, -1):
        b += a[i]
print('Сумма равна', b)