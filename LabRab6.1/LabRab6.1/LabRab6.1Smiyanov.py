def main():
    with open('LabRab61in.txt', 'r') as fin:
        i = 0
        w = 0
        l = []
        for line in fin:
            try:
                l.append(float(line))
            except ValueError:
                print('Следующая строка имеет неверный формат')
                print(line)
            else:
                i = i + 1
    if i < 3:
        print('Файл неверного формата (число строк верного формата меньше 3), изменения в файл внесены не будут')
    if i > 3:
        print('В файле больше 3 строк верного формата, будут использованы только первые 3 строки верного формата')
        calculation(l)
    if i == 3:
        calculation(l)
def calculation(l):
    a = l[0]
    b = l[1]
    c = l[2]
    if (a == 0) or (b == 0) or (c == 0) or (b+c == 0):
        with open('LabRab61out.txt', 'a') as fout:
            fout.write('Z1 не существует')
    else:
        z1 = ((1/a - 1/(b+c))/(1/a + 1/(b+c)))*(1 + (b*b + c*c - a*a)/2*b*c)/((a-b-c)/a*b*c)
        with open('LabRab61out.txt', 'a') as fout:
            fout.write('\nZ1 = {0: .3f} \n'.format(z1))
    z2 = ((a-b-c)/2)*a
    with open('LabRab61out.txt', 'a') as fout:
        fout.write('Z2 = {0: .3f} \n'.format(z2))
main()

