def z1(a, b, c):    
    if (a == 0) or (b == 0) or (c == 0) or (b+c == 0):
        z1 = '  -   '
    else:
        z1 = ((1/a - 1/(b+c))/(1/a + 1/(b+c)))*(1 + (b*b + c*c - a*a)/2*b*c)/((a-b-c)/a*b*c)
        z1 = '{0: 6.2f}'.format(z1)
    return z1
def z2(a, b, c):
    z2 = ((a-b-c)/2)*a
    z2 = '{0: 6.2f}'.format(z2)
    return z2
def main():
    with open('LabRab61out.txt', 'a') as fout:
        fout.write('+========+========+========+========+========+\n')
        fout.write('I   a    I   b    I   c    I   Z1   I   Z2   I\n')
        fout.write('+========+========+========+========+========+\n')    
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
                if (i % 3 == 0) and (i != 0):
                    with open('LabRab61out.txt', 'a') as fout:
                        a = l[i - 3]
                        b = l[i - 2]
                        c = l[i - 1]   
                        fout.write('I {0: 6.2f} I {1: 6.2f} I {2: 6.2f} I {3} I {4} I\n'.format(a, b, c, z1(a, b, c), z2(a, b, c)))
                        fout.write('+========+========+========+========+========+\n') 
                        print('Обновление файла - успешно')
main()