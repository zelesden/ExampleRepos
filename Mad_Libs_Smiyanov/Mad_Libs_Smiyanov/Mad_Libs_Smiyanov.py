# Mad Lib - Сумасшедшие истории

from tkinter import *

class Application(Frame):
    """  Графический интерфейс приложения """
    def __init__(self, master):
        """ Инициализация окна """
        super(Application, self).__init__(master)  
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Окно для ввода данных """
        # Инструкция
        Label(self,
              text = "Введите данные"
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)

        # Имя человека
        Label(self,
              text = "Имя: "
              ).grid(row = 1, column = 0, sticky = W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row = 1, column = 1, sticky = W)

        # Пол
        self.select_sex = StringVar()
        self.select_sex.set(None)
  
        # Выбор пола
        sexes = ['м', 'ж']
        column = 2
        for part in sexes:
            Radiobutton(self,
                        text = part,
                        variable = self.select_sex,
                        value = part
                        ).grid(row = 1, column = column, sticky = W)
            column += 1


        # Сущ.
        Label(self,
              text = "Существительное:"
              ).grid(row = 2, column = 0, sticky = W)
        self.noun_ent = Entry(self)
        self.noun_ent.grid(row = 2, column = 1, sticky = W)

        # Глагол
        Label(self,
              text = "Глагол (в н.ф.):"
              ).grid(row = 3, column = 0, sticky = W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row = 3, column = 1, sticky = W)
     
        # Прилагательное
        Label(self,
              text = "Имена прилагательные:"
              ).grid(row = 4, column = 0, sticky = W)

        # Чекбокс 
        self.is_strong_m = BooleanVar()
        Checkbutton(self,
                    text = "сильный",
                    variable = self.is_strong_m
                    ).grid(row = 4, column = 1, sticky = W)

        # Чекбокс
        self.is_funny_m = BooleanVar()
        Checkbutton(self,
                    text = "весёлый",
                    variable = self.is_funny_m
                    ).grid(row = 4, column = 2, sticky = W)

        # Чекбокс
        self.is_strong_w= BooleanVar()
        Checkbutton(self,
                    text = "сильная",
                    variable = self.is_strong_w
                    ).grid(row = 4, column = 3, sticky = W)

        # Чекбокс
        self.is_funny_w= BooleanVar()
        Checkbutton(self,
                    text = "весёлая",
                    variable = self.is_funny_w
                    ).grid(row = 4, column = 4, sticky = W)

        # Часть тела
        Label(self,
              text = "Часть тела:"
              ).grid(row = 5, column = 0, sticky = W)

        # Варианты выбора для каждой части тела
        self.body_part = StringVar()
        self.body_part.set(None)
  
        body_parts = ["нога", "голова", "рука"]
        column = 1
        for part in body_parts:
            Radiobutton(self,
                        text = part,
                        variable = self.body_part,
                        value = part
                        ).grid(row = 5, column = column, sticky = W)
            column += 1

        # создание кнопки
        Button(self,
               text = "Сгенерировать историю",
               command = self.tell_story
               ).grid(row = 6, column = 0, sticky = W)

        self.story_txt = Text(self, width = 75, height = 10, wrap = WORD)
        self.story_txt.grid(row = 7, column = 0, columnspan = 5)

    def tell_story(self):
        # получаем параметры из оболочки
        person = self.person_ent.get()
        noun = self.noun_ent.get()
        verb = self.verb_ent.get()
        adjectives = ""
        if self.is_strong_m.get():
            adjectives += "сильный, "
        if self.is_funny_m.get():
            adjectives += "весёлый, "
        if self.is_strong_w.get():
            adjectives += "сильная, "
        if self.is_funny_w.get():
            adjectives += "весёлая, "
        body_part = self.body_part.get()
        sex = self.select_sex.get()

        # генерируем историю
        if (sex == 'м'):
            story = 'Безработный '
        else:
            story = 'Безработная '
        story += person
        if (sex == 'м'):
            story += ' уже и не надеялся найти работу, как однажды он прочитал о компании "'
        else:
            story += ' уже и не надеялась найти работу, как однажды она прочитала о компании "'
        story += noun.title()
        story += '".'
        if (sex == 'м'):
            story += 'Энергичный, '
        else:
            story += 'Энергичная, '
        story += adjectives
        story += '.'       
        story += 'Наш герой отправился на собеседование в "'
        story += noun.title()        
        story += '". По дороге у героя'
        story += ' разболелась '        
        story += body_part + ". "
        story += 'На улице наш герой присел на '
        story += noun
        story += '. Позже '
        if (sex == 'м'):
            story += person + " вернулся домой. "
        else:
            story += person + " вернулась домой. "
        story += 'Мораль истории такова: "Не '
        story += verb
        story += ' перед собеседованием".'
        
        # вывод рассказа                           
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)

# main
root = Tk()
root.title("Mad Lib - Сумасшедшие истории")
app = Application(root)
root.mainloop()


