a = float(input('Введите a '))
b = float(input('Введите b '))
c = float(input('Введите с '))
if (a == 0) or (b == 0) or (c == 0) or (b+c == 0):
    z1 = '   -  '
else:
    z1 = ((1/a - 1/(b+c))/(1/a + 1/(b+c)))*(1 + (b*b + c*c - a*a)/2*b*c)/((a-b-c)/a*b*c)
    z1 = '{0: 6.2f}'.format(z1)
z2 = ((a-b-c)/2)*a
z2 = '{0: 6.2f}'.format(z2)
print('+========+========+========+========+========+')
print('I   a    I   b    I   c    I   Z1   I   Z2   I')
print('+========+========+========+========+========+')  
print('I {0: 6.2f} I {1: 6.2f} I {2: 6.2f} I {3} I {4} I'.format(a, b, c, z1, z2))
print('+========+========+========+========+========+') 
