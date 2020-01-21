import math
from fractions import Fraction
print('Введите Xbeg, Xend, Dx, Eps')
xb = float(input('Xbeg = '))
xe = float(input('Xend = '))
dx = float(input('Dx = '))
eps = float(input('Eps = '))
print('+---------+---------+------+')
print('I    X    I    Y    I   N  I')
print('+---------+---------+------+')
xt = xb
y = 0
ty = 1
while xb <= xe:
    x = xb
    y = 1
    n = 1
    top = 1
    down = 4
    while abs((x + 1)**0.25 - y) > eps:
        top = abs((((n-1)*4)-1) * top)
        down = down * 4 * n
        t = top/down
        ty = (x**n)*t
        if n%2 == 1:    
            y = y + ty
        elif n%2 == 0:
            y = y - ty
        n = n + 1
    print('I {0:7.2f} I {1: 7.2f} I {2: 4} I'. format(x, y, n))
    xb = xb + dx




