#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.
#максимальный ближе к 0!!!

from random import randint

a = [0 for i in range(20)]
for i in range(len(a)):
    a[i] = randint(-10, 10)

#print(a)

# Подсчитаем количесвто отрицательных элементов
b = 0
c = []
for i in range(len(a)):
    if a[i] < 0:
        b += 1
        c.append(i)
#print(b)

# создадим массив из этих отрицательных чисел
m = [0 for i in range(b)]
for i in range(len(m)):
    m[i] = a[c[i]]
#print(m)

# Найдем максимальное из этих отрицательных чисел
x = m[0]
for i in m:
    if x < i:
        x = i
print('Максимальное отрицательное число: ')
print(x)

# Остается найти индекс этого числа в первозданном массиве
z = []
for i in range(len(a)):
    if a[i] == x:
        z.append(i)
print('Данный элемент имеет индексы: ')
print(z)