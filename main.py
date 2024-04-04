import tkinter
from tkinter import *

infos, result = [], []


class MainWindow:
    def __init__(self, main):
        # Создаем кнопки
        self.exit_btn = Button(main, text="Выход",
                               font=15, bg="#bc4749",
                               fg="#2b2d42",
                               command=root.destroy
                               )
        self.open_file_btn = Button(main, text="Открыть",
                                    font=15, bg="#a7c957",
                                    fg="#2b2d42",
                                    )
        self.ask_btn = Button(main, text="Поиск",
                              font=15, bg="#a7c957",
                              fg="#2b2d42"
                              )

        # Создаем метки

        self.author_lb = Label(text="Курсовая работа студентки группы 23-ВТ-1 Матис О. О.",
                               font=15, bg="#8d99ae",
                               fg="#2b2d42"
                               )
        self.name_file_lb = Label(text="Введите имя файла:",
                                  font=15, bg="#8d99ae",
                                  fg="#2b2d42"
                                  )
        self.ask_lb = Label(text="Введите номер курса:",
                            font=15, bg="#8d99ae",
                            fg="#2b2d42"
                            )
        self.discipline_lb = Label(text="Полученные сведения:",
                                   font=15, bg="#8d99ae",
                                   fg="#2b2d42"
                                   )

        # Создаем текстовые поля для ввода

        self.name_file_ent = Entry(width=35,
                                   bg="#edf2f4",
                                   fg="#2b2d42"
                                   )
        self.ask_ent = Entry(width=35,
                             bg="#edf2f4",
                             fg="#2b2d42"
                             )
        # Создаем многострочное поле для вывода полученных данных
        self.discipline_txt = Text(width=70,
                                   height=10,
                                   bg="#edf2f4",
                                   fg="#2b2d42"
                                   )
        # Располагаем виджеты
        self.author_lb.grid(row=0, column=0,
                            columnspan=2,
                            stick="we", padx=5
                            )
        self.exit_btn.grid(row=0, column=3,
                           pady=5)
        self.open_file_btn.grid(row=1, column=2,
                                stick="we", padx=20)
        self.ask_btn.grid(row=2, column=2,
                          stick="we", padx=20)
        self.name_file_lb.grid(row=1, column=0,
                               stick="w", padx=5)
        self.ask_lb.grid(row=2, column=0,
                         stick="w", padx=5)
        self.discipline_lb.grid(row=3, column=0,
                                stick="we")
        self.name_file_ent.grid(row=1, column=1)
        self.ask_ent.grid(row=2, column=1)
        self.discipline_txt.grid(row=4, column=0,
                                 columnspan=5, padx=5)

        # Присваиваем функции кнопкам
        self.open_file_btn.bind("<Button-1>", self.open_file)
        self.ask_btn.bind("<Button-1>", self.search)

        # Создаем функции для кнопок

    def open_file(self, event):
        name_file = self.name_file_ent.get()
        try:
            file = open(name_file, "r", encoding="UTF-8")
            while True:
                info = file.readline().split()
                infos.append(info)
                if not info:
                    break
            file.close()
            self.discipline_txt.delete(1.0, END)
            self.discipline_txt.insert(1.0, f"Файл {name_file} открыт!")
        except FileNotFoundError:
            self.discipline_txt.delete(1.0, END)
            self.discipline_txt.insert(1.0, f"Файл {name_file} не найден!")

    def search(self, event):
        cnt = 0
        self.discipline_txt.delete(1.0, END)
        course = self.ask_ent.get()
        print(type(course))
        for i in range(len(infos) - 1):
            print(infos[i])
            if course == infos[i][2] and course in ["1", "2", "3", "4"]:
                self.discipline_txt.insert(1.0,
                                           f"Дисциплина: {infos[i][0]}; Часы: {infos[i][1]}; Отчет: {infos[i][3]}; Курс: {course} \n")
                cnt += 1
        if cnt == 0:
            self.discipline_txt.insert(1.0, "Такого курса нет в списке!")

root = Tk()
root.geometry("610x310")
root["bg"] = "#8d99ae"
root.resizable(False, False)
root.title("Получение сведений о дисциплинах и видах отчетности указанного курса")
q = MainWindow(root)
root.mainloop()
