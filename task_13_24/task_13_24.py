#Задача 13. Вариант 24
win = 0
c = '10'
f = ['0', '1', '2' , '3', '4', '5', '6', '7', '8', '9']


def introduction():
    print (
    '''
    Добро пожаловать в игру "Крестики - Нолики 2.0".
    Игра получила крупное обновление
    В этом релизе:
        1. Компьютер стал умнее, благодаря революционной технологии "Deep Mind"
        2. Теперь Вы можете играть с другом в новом режиме "PvP"
        3. Вам больше не нужно перезапускать приложение для запуска новой игры
        4. Раскладка и регистр больше не имеют значения
        5. Новая защита от падений
    Чтобы сделать ход - будет необходимо ввести номер клетки на поле
    Номера клеток представлены ниже:
    1|2|3
    4|5|6
    7|8|9
    '''
            )
def check_win():
    win = 0
    if (f[1] == f[2] == f[3] == 'X') or (f[4] == f[5] == f[6] == 'X' ) or (f[7] == f[8] == f[9] == 'X') or (f[1] == f[4] == f [7] == 'X') or (f[2] == f[5] == f[8] == 'X') or (f[3] == f[6] == f[9] == 'X') or (f[1] == f[5] == f[9] == 'X') or (f[3] == f[5] == f[7] == 'X'):
        win = 1
    if (f[1] == f[2] == f[3] == 'O') or (f[4] == f[5] == f[6] == 'O' ) or (f[7] == f[8] == f[9] == 'O') or (f[1] == f[4] == f [7] == 'O') or (f[2] == f[5] == f[8] == 'O') or (f[3] == f[6] == f[9] == 'O') or (f[1] == f[5] == f[9] == 'O') or (f[3] == f[5] == f[7] == 'O'):
        win = 2
    i = 1
    m = 0
    if (win == 0):
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
    sans = '0'
    ans = 0
    f [ans] = '0'
    field()
    while (f[ans] == 'X') or (f[ans] == 'O') or (f[ans] == '0'):  
        while (sans !='1') and (sans !='2') and (sans !='3') and (sans !='4') and (sans !='5') and (sans !='6') and (sans !='7') and (sans !='8') and (sans !='9'):
            sans = str(input('Введите номер клетки '))
        ans = int(sans)
        sans = '0'
    f[ans] = p
def computer_moves():
    move = 0
    best = [5, 1, 3, 7, 9, 2, 4, 6, 8]
    i = 0
    if (f[5] == 5) and (move == 0) and (f[5] != c) and (f[5] != p):
        f[5] = c
        move = 1
    if (f[1] == f[2]) and (move == 0) and (f[3] != c) and (f[3] != p):
        f[3] = c
        move = 1
    if (f[1] == [3]) and (move == 0) and (f[2] != c) and (f[2] != p):
        f[2] = c
        move = 1
    if (f[2] == f[3]) and (move == 0) and (f[1] != c) and (f[1] != p):
        f[1] = c
        move = 1
    if (f[4] == f[5]) and (move == 0) and (f[6] != c) and (f[6] != p):
        f[6] = c
        move = 1
    if (f[6] == f[5]) and (move == 0) and (f[4] != c) and (f[4] != p):
        f[4] = c
        move = 1
    if (f[4] == f[6]) and (move == 0) and (f[5] != c) and (f[5] != p):
        f[5] = c
        move = 1
    if (f[7] == f[8]) and (move == 0) and (f[9] != c) and (f[9] != p):
        f[9] = c
        move = 1
    if (f[7] == f[9]) and (move == 0) and (f[8] != c) and (f[8] != p):
        f[8] = c
        move = 1
    if (f[8] == f[9]) and (move == 0) and (f[7] != c) and (f[7] != p):
        f[7] = c
        move = 1
    if (f[1] == f[4]) and (move == 0) and (f[7] != c) and (f[7] != p):
        f[7] = c
        move = 1
    if (f[1] == f[7]) and (move == 0) and (f[4] != c) and (f[4] != p):
        f[4] = c
        move = 1
    if (f[4] == f[7]) and (move == 0) and (f[1] != c) and (f[1] != p):
        f[1] = c
        move = 1
    if (f[2] == f[5]) and (move == 0) and (f[8] != c) and (f[8] != p):
        f[8] = c
        move = 1
    if (f[8] == f[5]) and (move == 0) and (f[2] != c) and (f[2] != p):
        f[2] = c
        move = 1
    if (f[2] == f[8]) and (move == 0) and (f[5] != c) and (f[5] != p):
        f[5] = c
        move = 1
    if (f[3] == f[6]) and (move == 0) and (f[9] != c) and (f[9] != p):
        f[9] = c
        move = 1
    if (f[3] == f[9]) and (move == 0) and (f[6] != c) and (f[6] != p):
        f[6] = c
        move = 1
    if (f[6] == f[9]) and (move == 0) and (f[3] != c) and (f[3] != p):
        f[3] = c
        move = 1
    if (f[1] == f[5]) and (move == 0) and (f[9] != c) and (f[9] != p):
        f[9] = c
        move = 1
    if (f[1] == f[9]) and (move == 0) and (f[5] != c) and (f[5] != p):
        f[5] = c
        move = 1
    if (f[5] == f[9]) and (move == 0) and (f[1] != c) and (f[1] != p):
        f[1] = c
        move = 1
    if (f[3] == f[5]) and (move == 0) and (f[7] != c) and (f[7] != p):
        f[7] = c
        move = 1
    if (f[7] == f[5]) and (move == 0) and (f[3] != c) and (f[3] != p):
        f[3] = c
        move = 1
    if (f[3] == f[7]) and (move == 0) and (f[5] != c) and (f[5] != p):
        f[5] = c
        move = 1
    #Если нет угрозы победы игрока - компьютер ходит "набором лучших ходов"
    if (move == 0):
        while (f[best[i]] == 'X') or (f[best[i]] == 'O'):
            i = i + 1
        f [best[i]] = c
def X_O_choose():
    win = 0
    p = ' '
    while (p != 'X') and (p != 'O'):
        p = input('Выберите X или O ')
        p = p.upper()
        if (p == '0') or (p == 'О'):
            p = 'O'
        if (p == 'Х'):
            p = 'X'
    print ('Вы выбрали', p)
    return p

def PVE():
    #Внимание используются глобальные переменные p и c
    win = 0
    global p
    global c
    c = '10'
    p = X_O_choose()
    if p == 'X':
        c = 'O'
        while (win == 0):
            player_moves()
            win = check_win()
            if (win == 0):
                computer_moves()
                win = check_win()
        field()
        if (win == 1):
            print ('Вы победили')
        if (win == 2):
            print ('Компьютер победил')
        if (win == 3):
            print ('Ничья')
    if (p == 'O') or (p == '0'):
        c = 'X'
        while (win == 0):
            computer_moves()
            win = check_win()
            if (win == 0):
                player_moves()
                win = check_win()
        field()
        if (win == 2):
            print ('Вы победили')
        if (win == 1):
            print ('Компьютер победил')
        if (win == 3):
            print ('Ничья')
    game()
def PVP():
    #Внимание используются глобальная переменная p
    global p
    x = 'X'
    o = 'O'
    win = 0
    while (win == 0):
        print ('Ход X')
        p = x
        player_moves()
        win = check_win()
        if (win == 0):
            print ('Ход O')
            p = o
            player_moves()
            win = check_win()
    field()
    if (win == 1):
        print ('Победил X')
    if (win == 2):
        print ('Победил O')
    if (win == 3):
        print ('Ничья')
    game()
def game():
    gm = ' '
    while (gm != 'PVP') and (gm != 'PVE') and (gm != 'E') and (gm != 'ПВП') and (gm != 'ПВЕ') and (gm != 'Е'):
        gm = input ('Выберите режим: PvP (игрок против игрока), PvE (игрок против компьютера) \nИли введите E для выхода ')
        gm = gm.upper()
    i = 0
    for i in range (10):
        f[i] = i
    if (gm == 'PVP') or (gm == 'ПВП'):
        PVP()
    if (gm == 'PVE') or (gm == 'ПВЕ'):
        PVE()
introduction()
game()
#Smiyanov D. A.
#21.10.2018
