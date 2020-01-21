import sqlite3
import tkinter as tk
def validation(card_number):
    sum = 0
    card_number = card_number.replace(" ", "")
    print (card_number)
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
            print(card_number[i])
        if ((i+1) % 2 == (b-1)*(b-1)):
            sum = sum + int(card_number[i])
            print(card_number[i])
    return sum
def add_user(user, pas):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor
    cursor.execute("SELECT * FROM users WHERE USERNAME = ?", (user,))
    data=cursor.fetchone()
    if data is None:
        cursor.execute ("INSERT INTO users (?, ?)" (user, pas,))
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
    conn = sqlite3.connect(cards.db)
    cursor = conn.cursor
    cursor.execute("SELECT * FROM cards WHERE CARDNAME = ?", (card,))
    data=cursor.fetchone()
    if data is None:
        cursor.execute ("INSERT INTO cards (?)" (card,))
    else:
        return False
    conn.close()
def search_card(card):
    conn = sqlite3.connect(cards.db)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cards WHERE CARDNAME = ?", (card,))
    data=cursor.fetchone()
    if data is None:
        return False
    elif data[0] == card:
        return True
    else:
        return False
    conn.close()
