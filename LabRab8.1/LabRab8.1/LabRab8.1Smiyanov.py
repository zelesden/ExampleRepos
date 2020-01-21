# Функции:
# y = 1/3x - 2/3
# y = -1/3x +2/3
# y = ln|1/tg(x/2)|

import math
import pylab
from matplotlib import mlab
def func(x):
    if (x >= -5) and (x <= -2):
        y = -(x/3) - (2/3)
    elif (x <= 5) and (x >= 2):
        y = (x/3) - (2/3)
    elif (x > -2) and (x < 2):
        if x != 0:
            y = math.log(math.fabs(1/math.tan(x/2)))
        if x == 0:
            y = None
    else: 
        y = None
    return (y)
xmin = -5
xmax = 5
dx = 0.01
xlist = mlab.frange (xmin, xmax, dx)
ylist = [func(x) for x in xlist]
p1 = [(xmin - 1), (xmax + 1)]
p2 = [0, 0]
pylab.plot (p1, p2, color = 'black')
pylab.plot (p2, p1, color = 'black')
pylab.plot (xlist, ylist)
pylab.show()