import random
import array
def main():   
    with open('LabRab65in.txt', 'r') as fin:
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
                with open('LabRab65out.txt', 'a') as fout:   
                    fout.write('\nРазмер матрицы (N*N) = {0} \n'.format(N[i]))
                calculation(N[i])
                i = i + 1
                print('Обновление файла - успешно')
def calculation(n):
    a = list_init(n)
    b = new_list(a, n)
    overlaps(a, n)
def list_init(n):
    a = []
    with open('LabRab65out.txt', 'a') as fout:
        fout.write('\nИсходная матрица\n')
    for i in range (n):
        a.append([0] * n)
    for i in range (n):
        for j in range (n):
            a[i] [j] = random.randint(-10, 10)
            with open('LabRab65out.txt', 'a') as fout:
                fout.write("{0: 3.0f} ".format(a[i][j]))
        with open('LabRab65out.txt', 'a') as fout:
            fout.write('\n')
    return a
def new_list(a, n):
    b = []
    p = 0
    with open('LabRab65out.txt', 'a') as fout:
        fout.write('Вторая матрица\n')
    for i in range (n):
        b.append([0] * n)
    for i in range (n):
        for j in range (n):
            b[i][j] = a[j][i]
            with open('LabRab65out.txt', 'a') as fout:
                fout.write("{0: 3.0f} ".format(a[i][j]))
        with open('LabRab65out.txt', 'a') as fout:
            fout.write('\n')
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
                with open('LabRab65out.txt', 'a') as fout:
                    fout.write('Для числа {0: 3.0f} число повторений = {1}\n'.format(t, count))

main()