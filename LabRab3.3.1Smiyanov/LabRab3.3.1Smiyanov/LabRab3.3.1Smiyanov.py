import math
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
    n = 2
    t0 = 1
    t1 = 1/4
    tn = t1
    y = t0 + t1*x
    while abs((x + 1)**0.25 - y) > eps:
        tn *= (4*(n-1)-1)/(4*n)
        tx = (-1)**(n-1)*(x**n)*tn
        y += tx
        n += 1
    print('I {0:7.2f} I {1: 7.2f} I {2: 4} I'. format(x, y, n))
    xb = xb + dx
