"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""
x = ''

while x != '0':
    a, b = int(input('Введите число 1: ')), int(input('Введите число 2: '))
    i = 0
    while i != 1:
        x = input('Введите знак операции: ')
        if x == '/' or x == '*' or x == '-' or x == '+':
            if x == '/' and b != 0:
                print(a / b)
            elif x == '/' and b == 0:
                print('Деление на 0 не возможно!')
            if x == '*':
                print(a * b)
            if x == '-':
                print(a - b)
            if x == '+':
                print(a + b)
            i = 1
        elif x == '0':
            print('Выход из программы')
            break
        else:
            print('Введите другой знак операции!')
