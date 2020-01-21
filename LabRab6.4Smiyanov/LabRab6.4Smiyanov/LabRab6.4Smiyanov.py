import math
import random
def main():   
    with open('LabRab64in.txt', 'r') as fin:
        i = 0
        w = 0
        N = []
        for line in fin:
            try:
                N.append(int(line))
            except ValueError:
                print('Следующая строка имеет неверный формат')
                print(line)
            else:
                with open('LabRab64out.txt', 'a') as fout:   
                    fout.write('\nЭлементов в списке (N) = {0} \n'.format(N[i]))
                calculation(N[i])
                i = i + 1
                print('Обновление файла - успешно')
def calculation(N):
    a = -15
    max = -6
    min = 6
    templist = []
    l = []
    with open('LabRab64out.txt', 'a') as fout:
        fout.write('Начальное состояние массива\n')
    # Создаём массив
    for i in range (N):
        l.append(random.uniform(-5, 5))
        with open('LabRab64out.txt', 'a') as fout:
            fout.write("{0: 7.3f} ".format(l[i])) 
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
    with open('LabRab64out.txt', 'a') as fout:
        fout.write('\nМинимальный элемент = {0: 7.3f}\n'.format(min))
        fout.write('Максимальный элемент = {0: 7.3f}\n'.format(max))
    m = int((maxi - mini)//2)
    while (a > max) or (a < min):
        a = float(input('Введите a (при max >= a и min <= a) '))
    with open('LabRab64out.txt', 'a') as fout:
        fout.write('Пользователь ввёл: {0}\n'.format(a))
    # Делаем вставку элемента
    l.append(0)
    buf_in = a
    for i in range(mini +m +1, len(l)): 
        buf_out = l[i] 
        l[i] = buf_in 
        buf_in = buf_out 
    with open('LabRab64out.txt', 'a') as fout:
        fout.write('После вставки нового элемента\n')
    for i in range (len(l)):
        with open('LabRab64out.txt', 'a') as fout:
            fout.write("{0: 7.3f} ".format(l[i])) 
    print()
    i = 0
    with open('LabRab64out.txt', 'a') as fout:   
            fout.write('\nПосле сортировки по разности модулей\n')
    ll = list(map(lambda x: x-a, l))
    lll = list(zip(l,ll))
    llll = sorted(lll, key=lambda x: abs(x[1]))
    lllll = list(map(lambda x: x[0], llll))
    for i in range (len(l)):
        with open('LabRab64out.txt', 'a') as fout:           
            fout.write("{0: 7.3f} ".format(lllll[i]))
main()