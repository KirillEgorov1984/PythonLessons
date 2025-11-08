import tkinter as tk

class MyGUI:
    def __init__(self):
        # Создать виджет главного окна
        self.main_window = tk.Tk()
        # Создать две рамки: одну для верхней части окна,
        # другую для нижней части.
        self.top_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)
        # Создать три виджета Lable
        self.label1 = tk.Label(self.top_frame
                               ,text='Мигнуть')
        self.label2 = tk.Label(self.top_frame
                               , text='Моргнуть')
        self.label3 = tk.Label(self.top_frame
                               , text='Кивнуть')
        # Упаковать надписи, расположеные в верхней рамке
        # Применить аргумент side ='top', чтобы их
        # расположить одну под другой
        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')
        # Создать три виджета  Label
        # для нижней рамки.
        self.label4 = tk.Label(self.bottom_frame
                               , text='Мигнуть')
        self.label5 = tk.Label(self.bottom_frame
                               , text='Моргнуть')
        self.label6 = tk.Label(self.bottom_frame
                               , text='Кивнуть')
        # Упаковать надписи, расположенные в нижней рамке.
        # Применить аргумент side='left', чтобы их
        # расположить горизонтально слева в рамке.
        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')
        # Упаковываем рамки
        self.top_frame.pack()
        self.bottom_frame.pack()
        # Вход в главный цикл tkinter
        tk.mainloop()
        # Создать экземпляр класса MyGUI
if __name__ =='__main__':
    my_gui = MyGUI()