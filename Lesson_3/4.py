# 4.	Определить, какое число в массиве встречается чаще всего.

# Создадим массив случайных чисел:

from random import randint

a = [0 for i in range(20)]
for i in range(len(a)):
    a[i] = randint(0, 20)
print('Массив случайных чисел: ')
print(a)
# посчитаем количество каждого числа в массиве
b = 0
c = []
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] == a[j]:
            b += 1
    c.append(b)
    b = 0
print('Количество повторений каждого элемента в массиве:')
print(c)

# найдем макимальное количество повторений:
x = 0
for i in range(len(c)):
    if x < c[i]:
        x = c[i]
# найдем числа, имеющие максимальное число повторений:
z = []
for i in range(len(c)):
    if c[i] == x:
        if not a[i] in z:
            z.append(a[i])

print('Максимальное число повторений имеет число:', z)