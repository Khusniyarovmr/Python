"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""
from random import randint

a = [0 for i in range(20)]
for i in range(len(a)):
    a[i] = randint(0, 20)

print(a)
# Найдем первое минимальное значение
y = 100
yi = []
for i in range(len(a)):
    if y > a[i]:
        y = a[i]

# проверим нужно ли искать другое минимальное число
for i in a:
    if i == y:
        yi.append(i)
if len(yi) > 1:
    print('Наименьшие число: ', y)
else:
    x = 100
    for i in range(len(a)):
        if x > a[i] and a[i] != y:
            x = a[i]
    print('Наименьшие числа: ', y, x)
