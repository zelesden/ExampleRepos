from tkinter import *
import operator
import csv
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

        # ФИО
        Label(self,
              text = "Фамилия ИО/Имя нового файла: "
              ).grid(row = 1, column = 0, sticky = W)
        self.name = Entry(self)
        self.name.grid(row = 1, column = 1, sticky = W)


        # Должность
        Label(self,
              text = "Должность:"
              ).grid(row = 2, column = 0, sticky = W)
        self.job = Entry(self)
        self.job.grid(row = 2, column = 1, sticky = W)

        # Год
        Label(self,
              text = "Год поступления на работу:"
              ).grid(row = 3, column = 0, sticky = W)
        self.year = Entry(self)
        self.year.grid(row = 3, column = 1, sticky = W)

        # Оклад
        Label(self,
              text = "Оклад:"
              ).grid(row = 4, column = 0, sticky = W)
        self.salary = Entry(self)
        self.salary.grid(row = 4, column = 1, sticky = W)

        # Добавить
        Button(self,
               text = "Добавить",
               command = self.add
               ).grid(row = 6, column = 0, sticky = W)

        self.story_txt = Text(self, width = 75, height = 10, wrap = WORD)
        self.story_txt.grid(row = 8, column = 0, columnspan = 5)


        # Сортировка
        Button(self,
               text = "Сортировка",
               command = self.sorting
               ).grid(row = 7, column = 0, sticky = W)


        # О служащем
        Button(self,
               text = "Подробная информация по фамилии и ИО",
               command = self.about
               ).grid(row = 6, column = 2, sticky = W)
                # О служащем
        Button(self,
               text = "Форматирование файла",
               command = self.format
               ).grid(row = 7, column = 2, sticky = W)
        Button(self,
               text = "Новый файл",
               command = self.new
               ).grid(row = 6, column = 3, sticky = W)

    def add(self):
        f = 'LabRab71.csv'
        name = self.name.get()
        job = self.job.get()
        year = self.year.get()
        salary = self.salary.get()
        inf = [name, job, year, salary]
        with open (f, 'a', newline = '\n') as file:
            writer = csv.writer(file, delimiter =';')
            writer.writerow(inf)
        text = name + ' ' + job + ' ' + year + ' ' + salary + ' добавлен(а)\n'       
        # вывод текста                           
        self.story_txt.insert(0.0, text)
    def format(self):
        f = 'LabRab71.csv'
        inf = ['Имя', 'Должность', 'Год', 'Оклад']
        with open (f, 'w', newline = '\n') as file:
            writer = csv.writer(file, delimiter =';')
            writer.writerow(inf)
        text = "Файл отформатирован"
        self.story_txt.insert(0.0, text)
    def sorting(self):
        data = []
        with open('LabRab71.csv', 'r') as f:
            for row in csv.reader(f):
                data.append(convert(types, row))
        data.sort(key=operator.itemgetter('Имя'))
        with open('LabRab71.csv', 'w') as f:
            csv.writer(f).writerows(data)

    def sort_(self):
        f = 'LabRab71.csv'
        with open(f,newline='\n') as file:
            spamreader = csv.DictReader(file, delimiter=";")
            sortedlist = sorted(spamreader, key=lambda row:(row['Имя'],row['Должность'], row['Год'], row ['Оклад']), reverse=False)
        with open(f,'w', newline='\n') as file:
            writer = csv.writer(file, delimiter =';')
            writer.writerow(sortedlist)            
        
    def new(self):
        f = 'LabRab71.csv'
        name = self.name.get()
        nf = name + '.csv'
        with open (nf, 'w') as fout:
            None
        with open (f, 'r') as fin:
            for lin in (fin):
                with open(nf, 'a') as fout:
                    fout.write(lin)
        text = "Файл " + name + " создан"
        self.story_txt.insert(0.0, text)
    def about(self):
        f = 'LabRab71.csv'
        n = 0
        name = self.name.get()
        with open (f, 'r', newline = '\n') as file:
            reader = csv.reader(file, delimiter =';')
            for line in file:
                i = 0
                str = ''
                while line[i] != ';':
                    str = str + line[i]
                    i = i + 1
                if name == str:
                    line = line + '\n'
                    self.story_txt.insert(0.0, line)
                    

# main
root = Tk()
root.title("LabRab7.1")
app = Application(root)
root.mainloop()
