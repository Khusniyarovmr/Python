#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

# Создадим массив случайных чисел:

from random import randint

a = [0 for i in range(20)]
for i in range(len(a)):
    a[i] = randint(0, 20)
print('Было:')
print(a)
# Найдем минимальное и максимальное значение в полученном массиве:

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

# x - max (index = xi), y - min (index = yi).
# Меняем элементы местами:

a[xi], a[yi] = a[yi], a[xi]
print('Стало:')
print(a)
