import math
import pylab
from matplotlib import mlab
import random
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

R = float(input('Введите r '))
xmin = -R + 0.01
xmax = R - 0.01
dx = 0.01
xlist = mlab.frange (xmin, xmax, dx)
ylist = [func(R, x) for x in xlist]
mylist =[-func(R, -x) for x in xlist]
p1 = [(xmin - 1), (xmax + 1)]
p2 = [0, 0]
p3 = [-R, R]
p4 = [-R, -R]
p5 = [R, R]
pylab.plot (p1, p2, color = 'black')
pylab.plot (p2, p1, color = 'black')
pylab.plot (p4, p3, color = 'blue')
pylab.plot (p5, p3, color = 'blue')
pylab.plot (p3, p4, color = 'blue')
pylab.plot (p3, p5, color = 'blue')
pylab.plot (xlist, ylist, color = 'blue')
pylab.plot (xlist, mylist, color = 'blue')
for i in range (1000):
    flag = 0
    x = random.uniform(-R-2, R+2)
    y = random.uniform(-R-2, R+2)
    if ((x > 0) and (y > 0)):
        if (y >= (R - x)) and (y <= R) and (x <= R):
            flag = 1
    if ((x < 0) and (y < 0)) and (flag!= 1):
        if (y <= (-R - x)) and (-y <= R ) and (-x <= R):
            flag = 1
    if ((x > 0) and (y < 0)) and (flag != 1):
        if (y**2 >= R**2 - x**2) and (x <= R) and (-y <= R):
            flag = 1
    if ((x < 0) and (y > 0)) and (flag != 1) and (y <= R) and (-x <= R):
        if (y**2 >= R**2 - x**2):
            flag = 1
    if (flag == 1):
        pylab.scatter(x, y, color = 'green')
    if (flag == 0):
        pylab.scatter(x, y, color = 'red')
pylab.show()