# Функции:
# y = 1/3x - 2/3
# y = -1/3x +2/3
# y = ln|1/tg(x/2)|

import math
x = float(input('Введите x '))
if (x >= -5) and (x <= -2):
    y = -(x/3) + (2/3)
elif (x <= 5) and (x >= 2):
    y = (x/3) - (2/3)
elif (x > -2) and (x < 2):
    try:
        y = math.log(math.fabs(1/math.tan(x/2)))
    except ZeroDivisionError:
        print ('x не входит в область определения функции ')
    else:
        print('y = ', y)
else:
    print ('x не входит в область определения функции ')