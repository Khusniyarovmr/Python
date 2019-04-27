# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
N = 98
x = [0] * N
for i in range(N):
    x[i] = i + 2

a = [[0 for i in range(2)] for j in range(2, 10)]

for i in range(8):
    a[i][0] = i+2

for j in range(2,10):
    for i in x:
        if i % j == 0:
            a[j-2][1] += 1

print('Число - делитель|количество кратных чисел')
for j in range(len(a)):
    for i in range(2):
        print(a[j][i], end=' | ')
    print()