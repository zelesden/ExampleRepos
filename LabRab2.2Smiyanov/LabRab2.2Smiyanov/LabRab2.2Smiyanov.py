# y = R - x | ((x > 0) and (y > 0)) or ((x < 0) and (y < 0))
# y**2 = R**2 - x**2 | ((x > 0) and (y < 0)) or ((x < 0) and (y > 0))

import math

R = float(input('Введите R '))
x = float(input('Введите x '))
y = float(input('Введите y '))
a = 0
if ((x > 0) and (y > 0) and (R > x) and (R > y)):
    if (y > (R - x)) and (y <= R):
        print ('Входит')
        a = 1
if ((x < 0) and (y < 0)) and (a != 1) and (-R < x) and (-R < y):
    if (y < (R - x)) and (y >= -R ):
        print ('Входит')
        a = 1
if (((x > 0) and (y < 0)) or ((x < 0) and (y > 0))) and (a != 1) and (math.fabs(R) > math.fabs(x)) and (math.fabs(R) > math.fabs(y)):
    if (y**2 > R**2 - x**2):
        print ('Входит')
        a = 1
if (a == 0):
    print ('Не входит')