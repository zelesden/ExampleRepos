# Функции:
# y = 1/3x - 2/3
# y = -1/3x +2/3
# y = ln|1/tg(x/2)|

import math
x = float(input('Введите начальный x '))
xend = float(input('Введите конечный x '))
d = float(input('Введите шаг '))
print('+---------+---------+')
print('I    X    I    Y    I')
while x <= xend:
    y = 4
    if (x >= -5) and (x <= -2):
        y = -(x/3) + (2/3)
    elif (x <= 5) and (x >= 2):
        y = (x/3) - (2/3)
    elif (x > -2) and (x < 2) and (x != 0):
        y = math.log(math.fabs(1/math.tan(x/2)))
    if (y != 4):
        yf = '{0: 7.2f}'.format(y)
    if (y == 4):
        yf = '    -    '
    print('I {0: 7.2f} I {1: 7.2f} I'.format(x,y))
    x = x + d
