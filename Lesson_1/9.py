# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).
print('Введите три разных числа:')
a, b, c = int(input()), int(input()), int(input())
if a > b:
    if a > c:
        if c > b:
            x = c
        else:
            x = b
    else:
        x = a
else:
    if b > c:
        if a > c:
            x = a
        else:
            x = c
    else:
        x = b
print(x)
