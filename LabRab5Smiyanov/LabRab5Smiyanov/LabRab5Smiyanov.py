import random
#import array
def main():
    n = int(input('Введите размер марицы (N*N) '))
    a = list_init(n)
    b = new_list(a, n)
    overlaps(a, n)
def list_init(n):
    a = []
    print('Исходная матрица')
    for i in range (n):
        a.append([0] * n)
    for i in range (n):
        for j in range (n):
            a[i] [j] = random.randint(-10, 10)
            print("{0: 3.0f}".format(a[i][j]), end = ' ')
        print('')
    return a
def new_list(a, n):
    b = []
    p = 0
    print('Вторая матрица')
    for i in range (n):
        b.append([0] * n)
    for i in range (n):
        for j in range (n):
            b[i][j] = a[j][i]
            print("{0: 3.0f}".format(b[i][j]), end = ' ')
        print()
    return b
def overlaps(a, n):
    c = a
    for i in range (n):
        for j in range (n):
            count = 0
            t = c[i][j]
            if t != 11:
                for i1 in range (n):
                    for j1 in range (n):
                        if t == c[i1][j1]:
                            count = count + 1
                            c[i1][j1] = 11
                print('Для числа', t, 'число повторений =', count)

main()