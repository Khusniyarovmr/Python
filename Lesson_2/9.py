"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""
n = input('Введите натуральные числа через пробел: ')
n = n.split()
a = 0
b = 0
for i in n:
    for j in range(len(i)):
        a += int(i[j])
    if a > b:
        b = a
    a = 0
print(b)