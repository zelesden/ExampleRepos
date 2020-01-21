import math
import pylab
from matplotlib import mlab
def func(R, x):
    if ((x >= 0) and ((R - x) >= 0)) and (x < R):
        y = R - x
    elif ((x > 0) and ((math.sqrt(R**2 - x**2)) < 0)) and (x < R):
        y = math.sqrt(R**2 - x**2)
    elif ((x < 0) and ((math.sqrt(R**2 - x**2)) > 0)) and (x < R):
        y = math.sqrt(R**2 - x**2)
    elif ((x <= 0) and ((x - R) <= 0)) and (x < R):
        y = x - R
    else:
        y = 0
    return y

r = float(input('Введите r '))
xmin = -r + 0.01
xmax = r - 0.01
dx = 0.01
xlist = mlab.frange (xmin, xmax, dx)
ylist = [func(r, x) for x in xlist]
mylist =[-func(r, -x) for x in xlist]
p1 = [(xmin - 1), (xmax + 1)]
p2 = [0, 0]
p3 = [-r, r]
p4 = [-r, -r]
p5 = [r, r]
pylab.plot (p1, p2, color = 'black')
pylab.plot (p2, p1, color = 'black')
pylab.plot (p4, p3, color = 'blue')
pylab.plot (p5, p3, color = 'blue')
pylab.plot (p3, p4, color = 'blue')
pylab.plot (p3, p5, color = 'blue')
pylab.plot (xlist, ylist, color = 'blue')
pylab.plot (xlist, mylist, color = 'blue')
x = xmin
while x < xmax:
    y = func(r, x)
    p6 = [r, y]
    p7 = [x, x]
    pylab.plot(p7, p6, color = 'blue')
    y = -func(r, -x)
    p6 = [y, -r]
    pylab.plot(p7, p6, color = 'blue')
    x = x + dx
pylab.show()
