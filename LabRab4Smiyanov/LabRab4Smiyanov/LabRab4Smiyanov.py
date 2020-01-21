import math
import random
N = 0
a = -15
max = -6
min = 6
templist = []
while ((N < 5) and (N < 30)):
    N = int(input('Введите число элементов списка (не больше 30, не меньше 5) '))
l = []
print('Начальное состояние массива')
# Создаём массив
for i in range (N):
    l.append(random.uniform(-5, 5))
    print ("{0: 7.3f}".format(l[i]), end = '  ') 
print()
# Ищем максимальный и минимальный элементы, а также их индексы
for i in range (N):
    if (l[i] > max):
        max = l[i]
        maxi = i
    if (l[i] < min):
        min = l[i]
        mini = i
if (maxi < mini):
    t = maxi
    maxi = mini
    mini = t

print('Минимальный элемент = ', "{0: 7.3f}".format(min))
print('Максимальный элемент = ', "{0: 7.3f}".format(max))
m = int((maxi - mini)//2)
while (a > max) or (a < min):
    a = float(input('Введите a (при max >= a и min <= a) '))
print('После вставки нового элемента')
# Делаем вставку элемента
l.append(0)
buf_in = a
for i in range(mini +m +1, len(l)): 
    buf_out = l[i] 
    l[i] = buf_in 
    buf_in = buf_out 
for i in range (len(l)):
    print ("{0: 7.3f}".format(l[i]), end = '  ') 
print()
i = 0
print('После сортировки по разности модулей')
ll = list(map(lambda x: x-a, l))
lll = list(zip(l,ll))
llll = sorted(lll, key=lambda x: abs(x[1]))
lllll = list(map(lambda x: x[0], llll))
for i in range (len(l)):
    print ("{0: 7.3f}".format(lllll[i]), end = '  ')
print()



        
