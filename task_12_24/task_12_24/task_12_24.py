#Задача 12. Вариант 24
win = 0
p = ' '
c = '10'
f = ['0', '1', '2' , '3', '4', '5', '6', '7', '8', '9']

def introduction():
    print (
    '''
    Добро пожаловать в игру "Крестики - Нолики".
    Вы будете играть с компьютером.
    Чтобы сделать ход - будет необходимо ввести номер клетки на поле.
    Номера клеток представлены ниже:
    1|2|3
    4|5|6
    7|8|9
    '''
            )
def check_win(win):
    win = 0
    if (f[1] == f[2] == f[3] == 'X') or (f[4] == f[5] == f[6] == 'X' ) or (f[7] == f[8] == f[9] == 'X') or (f[1] == f[4] == f [7] == 'X') or (f[2] == f[5] == f[8] == 'X') or (f[3] == f[6] == f[9] == 'X') or (f[1] == f[5] == f[9] == 'X') or (f[3] == f[5] == f[7] == 'X'):
        win = 1
    if (f[1] == f[2] == f[3] == 'O') or (f[4] == f[5] == f[6] == 'O' ) or (f[7] == f[8] == f[9] == 'O') or (f[1] == f[4] == f [7] == 'O') or (f[2] == f[5] == f[8] == 'O') or (f[3] == f[6] == f[9] == 'O') or (f[1] == f[5] == f[9] == 'O') or (f[3] == f[5] == f[7] == 'O'):
        win = 2
    i = 1
    m = 0
    while (i < 10):
        if (f[i] == 'X') or (f[i] == 'O'):
            m = m + 1
        i = i + 1
    if (m == 9):
        win = 3
    return win
def field():
        print ( f[1], '|', f[2], '|', f[3])
        print ( f[4], '|', f[5], '|', f[6])
        print ( f[7], '|', f[8], '|', f[9])    
def player_moves():
    ans = 0
    f [ans] = '0'
    field()
    while (f[ans] == 'X') or (f[ans] == 'O') or (f[ans] == '0'):  
        ans = int(input('Введите номер клетки '))
    f[ans] = p
def computer_moves():
    i = 0
    best = [5, 1, 3, 7, 9, 2, 4, 6, 8]
    while (f[best[i]] == 'X') or (f[best[i]] == 'O'):
        i = i + 1
    f [best[i]] = c
def X_O_choose(p):
    p = ' '
    while (p != 'X') and (p != 'O'):
        p = input('Выберите X (англ. икс) или O (англ. оу) ')
    print ('Вы выбрали', p)
    return p
introduction()
p = X_O_choose(p)
if p == 'X':
    c = 'O'
    while (win == 0):
        player_moves()
        win = check_win(win)
        if (win == 0):
            computer_moves()
            win = check_win(win)
    field()
    if (win == 1):
        print ('Вы победили')
    if (win == 2):
        print ('Компьютер победил')
    if (win == 3):
        print ('Ничья')
if p == 'O':
    c = 'X'
    while (win == 0):
        computer_moves()
        win = check_win(win)
        if (win == 0):
            player_moves()
            win = check_win(win)
    field()
    if (win == 2):
        print ('Вы победили')
    if (win == 1):
        print ('Компьютер победил')
    if (win == 3):
        print ('Ничья')
input('Press Enter to exit')

#Smiyanov D. A.
#21.10.2018

