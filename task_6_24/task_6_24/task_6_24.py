# Задача 6. Вариант 24.
import random
a = ['гнедая', 'рыжая', 'серая', 'вороная']
b = random.randint(0,3)
player = input('Введите масть ')
if (a[b] == player):
    print ('Вы выиграли')
else:
    print ('Вы проиграли, компьютер загадал масть:', a[b])
input('Press Enter to exit')

#Smiyanov D. A.
#06.09.2018

