import tkinter as tk

class MyGUI:
    def __init__(self):
        # Создание виджета главного окна
        self.main_window = tk.Tk()

        # Создать два виджета Lable
        self.label1 = tk.Label(self.main_window,
                               text='Привет, мир!',
                               borderwidth = 1, relief= 'solid')
        self.label2 = tk.Label(self.main_window,
                               text='sunken',
                               borderwidth = 1, relief= 'solid')


        # Показать заголовок и вызвать метод pack виджетов Lebel, опеределение на листе и отсупы
        self.label1.pack(ipadx=20, ipady=20) # внутреннее заполнение
        self.label2.pack(ipadx=20, ipady=20) # внутреннее заполнение

        # Вход в главный цикл tkinter
        tk.mainloop()
        # Создать экземпляр класса MyGUI
if __name__ =='__main__':
    my_gui = MyGUI()