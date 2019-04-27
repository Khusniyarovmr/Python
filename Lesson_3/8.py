"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

n = 5
m = 4
A = [[0 for i in range(m)] for j in range(n)]
#print(A)

for i in range(len(A)):
    S = input('Введите 3 числа через пробел').split()
    for j in range(len(S)):
        A[i][j] = S[j]
#print(A)

for i in range(len(A)):
    s = 0
    for j in A[i]:
        s += int(j)
    A[i][3] = s
#print(A)

for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end=' ')
    print()


