# Доделать реализовать чтобы пользователь вводил с клавиатуры 5 чисел подряд
"""def fact2(n): 
    if n % 2 == 0:
        f = 1
        for i in range(2, n+1, 2):
            f *= i
        print(f"Двойной факториал из {i} - {f}")

    elif n % 2 != 0:
        f = 1
        for i in range(1, n+1, 2):
            f *= i
        print(f"Двойной факториал из {i} - {f}")"""


# Задание 2

import math
import random
a = 'Заказ'
b = 'Радар'
c = 'Церковь'


"""def pol(x):
    x = x.lower()
    if x == x[::-1]:
        print('Polindrom')
    else:
        print('Ne polindrom')


pol(c)"""


# 3
def sin1(x, eps):
    if eps <= 0:
        print('Dolzno bit bolshe 0')
        y = x
        f = x
        i = 3
        while abs(y) > eps:
            y *= (-1)*x * x / ((i-1)*i)
            i += 2
            f += y
        return f


eps = 0.01
for i in range(0, 6):
    x = math.pi/4
    print('eps= ', eps, '; sin(', x, ') = ', sin1(x, eps), ";", math.sin(x))


sin1(2, 6)
