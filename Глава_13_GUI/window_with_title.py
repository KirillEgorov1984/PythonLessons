import tkinter as tk

class MyGUI:
    def __init__(self):
        #Создание виджета главного окна
        self.main_window = tk.Tk()
        #Показать заголовок
        self.main_window.title('Мой первый GUI')
        #Вход в главный цикл tkinter
        tk.mainloop()
        #Создать экземпляр класса MyGUI
if __name__ =='__main__':
    my_gui = MyGUI()

