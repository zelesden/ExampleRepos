import math
import pylab
from matplotlib import mlab
def func1(x, b):
    y = math.atan(x) + b
    return (y)
def func2(xb, xe, dx, eps, x):
    xt = xb
    y = 0
    ty = 1
    while xb <= xe:
        x = xb
        n = 0
        y = math.pi
        tn = 1/x
        while abs(tn) > eps:
            tn = (-1)**(n+1)/((2*n+1)*x**(2*n+1))
            y += tn
            n += 1
        xb = xb + dx
        return (y)
xmin = -5
xmax = 5
dx = 0.01
esp = 0.1
b = float(input('Введите b '))
xlist = mlab.frange (xmin, xmax, dx)
ylist = [func1(x, b) for x in xlist]
ylist2 = [func2(xmin, xmax, dx, esp, x) for x in xlist]
p1 = [(xmin - 1), (xmax + 1)]
p2 = [0, 0]
pylab.plot (p1, p2, color = 'black')
pylab.plot (p2, p1, color = 'black')
pylab.plot (xlist, ylist)
pylab.plot (xlist, ylist2)
pylab.show()
