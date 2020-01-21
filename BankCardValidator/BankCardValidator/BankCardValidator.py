import sqlite3
import tkinter as tk
def validation(card_number):
    sum = 0
    card_number = card_number.replace(" ", "")
    N = len(card_number)
    if (N % 2 == 0):
        b = 1
    else: 
        b = 0
    for i in range (N):
        if ((i+1) % 2 == b):
            t = 2*int(card_number[i])
            if t > 9:
                t = t - 9
            sum = sum + t
        if ((i+1) % 2 == (b-1)*(b-1)):
            sum = sum + int(card_number[i])
    return sum
def add_user(user, pas):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor
    cursor.execute("SELECT * FROM users WHERE USERNAME = ?", (user,))
    data=cursor.fetchone()
    if data is None:
        cursor.execute ("INSERT INTO users (?, ?)", (user, pas,))
    else:
        return False
    conn.close()
def log_in(user, pas):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE USERNAME = ?", (user,))
    data=cursor.fetchone()
    if data is None:
        return False
    elif data[1] == pas:
        return True
    else:
        return False
    conn.close()
def add_card(card):
    conn = sqlite3.connect("cards.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cards WHERE CARDNAME = ?", (card,))
    data=cursor.fetchone()
    if data is None:
        cursor.execute ("INSERT INTO cards(CARDNAME) VALUES(?);", (card,))
    else:
        return False
    conn.close()
def search_card(card):
    conn = sqlite3.connect("cards.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cards WHERE CARDNAME = ?", (card,))
    data=cursor.fetchone()
    print(data[0])
    print(data[1])
    if data is None:
        return False
    elif data[0] == card:
        return True
    else:
        return False
    conn.close()
#вставка
class Main_w:
    import Func
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.labelN = tk.Label(self.frame, text = 'Номер карты',font = 'Arial 12', width = 20).grid(row = 0, column = 0)
        self.text1= tk.Text(self.frame,height = 1,width=20,font='Arial 12')
        self.text1.grid(row = 0, column = 1)
        self.button1 = tk.Button(self.frame, text = 'Поиск', width = 20,  command = self.new_search).grid(row = 1, column = 0)
        self.button2 = tk.Button(self.frame, text = 'Проверка', width = 20,  command = self.new_check).grid(row = 1, column = 1)
        self.button3 = tk.Button(self.frame, text = 'Сменить пользователя', width = 20,  command = self.new_change).grid(row = 1, column = 2)
        self.labelS = tk.Label(self.frame, text = 'Платёжная система',font = 'Arial 12', width = 20).grid(row = 2, column = 0)
        self.label2= tk.Label(self.frame, text = '', height = 1,width=20,font='Arial 12').grid(row = 2, column = 1)
        self.labelC = tk.Label(self.frame, text = 'Валидация',font = 'Arial 12', width = 20).grid(row = 3, column = 0)
        self.label3 = tk.Label(self.frame,text = '', height = 1,width=20,font='Arial 12').grid(row = 3, column = 1)
        self.frame.pack()

    def new_search(self):
        card = self.text1.get("1.0", "end-1c")
        if search_card(card):
            self.newWindow = tk.Toplevel(self.master)
            self.app = Tsearch_result(self.newWindow)
    def new_check(self):
        card = self.text1.get("1.0","end-1c")
        ch = validation(card)
        if ch % 10 == 0:
            print(ch)
            print(card[0])
            if card[0] == '3':
                self.label2= tk.Label(self.frame, text = 'American Express', height = 1,width=20,font='Arial 12').grid(row = 2, column = 1)
            if card[0] == '4':
                self.label2= tk.Label(self.frame, text = 'Visa', height = 1,width=20,font='Arial 12').grid(row = 2, column = 1)
            if card[0] == '5':
                self.label2= tk.Label(self.frame, text = 'MasterCard', height = 1,width=20,font='Arial 12').grid(row = 2, column = 1)
            self.label3 = tk.Label(self.frame, text = 'Карта валидна', height = 1,width=20,font='Arial 12').grid(row = 3, column = 1)
            card = int(card)
            add_card(card)
        else:
            self.label3 = tk.Label(self.frame, text = 'Карта не валидна', height = 1,width=20,font='Arial 12').grid(row = 3, column = 1)
    def new_change(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Log_in_w(self.newWindow)

class Log_in_w:
    import Func
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.labelN = tk.Label(self.frame, text = 'Имя пользователя',font = 'Arial 12', width = 20).grid(row = 0, column = 0)
        self.tUser= tk.Text(self.frame,height = 1,width=20,font='Arial 12')
        self.tUser.grid(row = 0, column = 1)
        self.labelN = tk.Label(self.frame, text = 'Пароль',font = 'Arial 12', width = 20).grid(row = 1, column = 0)
        self.tPass= tk.Text(self.frame,height = 1,width=20,font='Arial 12')
        self.tPass.grid(row = 1, column = 1)
        self.label0 = tk.Label(self.frame, text = '',font = 'Arial 12', width = 20).grid(row = 2, column = 0)
        self.bLog_in = tk.Button(self.frame, text = 'Войти', width = 20, command = self.log).grid(row = 3, column = 0)
        self.frame.pack()

    def log(self):
        user = self.tUser.get("1.0","end-1c")
        pas = self.tPass.get("1.0", "end-1c")
        if log_in(user, pas):
            self.new_main()
            #self.master.destroy()
        else:
            self.label0 = tk.Label(self.frame, text = 'Отказ',font = 'Arial 12', width = 20).grid(row = 2, column = 0)


    def new_main(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Main_w(self.newWindow)
class Tsearch_result:
    import Func
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.labelN = tk.Label(self.frame, text = 'Карта найдена',font = 'Arial 12', width = 20).grid(row = 0, column = 0)
class Fsearch_result:
    import Func
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.labelN = tk.Label(self.frame, text = 'Карта не найдена',font = 'Arial 12', width = 20).grid(row = 0, column = 0)
def main(): 
    root = tk.Tk()
    app = Log_in_w(root)
    root.mainloop()

if __name__ == '__main__':
    main()
#Вставка



   

