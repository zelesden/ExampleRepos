# y = R - x | ((x > 0) and (y > 0)) or ((x < 0) and (y < 0))
# y**2 = R**2 - x**2 | ((x > 0) and (y < 0)) or ((x < 0) and (y > 0))

import math
import random
R = float(input('Введите R '))
print('   X       Y    Res')
print('-------------------')
for i in range (10):
    flag = 0
    x = random.uniform(-R, R)
    y = random.uniform(-R, R)
    print("{0: 7.2f} {1: 7.2f}".format(x, y), end = ' ')
    if ((x >= 0) and (y >= 0)):
        if (y >= (R - x)) and (y <= R):
            flag = 1
    if ((x <= 0) and (y <= 0)) and (flag!= 1):
        if (y <= (R - x)) and (y >= -R ):
            flag = 1
    if (((x > 0) and (y < 0)) or ((x < 0) and (y > 0))) and (flag != 1):
        if (y**2 >= R**2 - x**2):
            flag = 1
    if (flag == 1):
        print('Yes')
    if (flag == 0):
        print('No')
