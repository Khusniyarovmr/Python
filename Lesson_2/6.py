"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""
from random import randint

x = randint(0,100)
f = False

for i in range(10):
    y = int(input('Введите число: '))
    if y == x:
        print('Молодец! Вы отгадали число!', 'Это число: ', x)
        f = True
        break

if f == False:
    print('Загаданное программой число:', x)