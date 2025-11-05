import tkinter as tk

class MyGUI:
    def __init__(self):
        # Создание виджета главного окна
        self.main_window = tk.Tk()
        self.main_window.title('Мой первый GUI')
        # --- Задаем размеры окна ---
        window_width = 800
        window_height = 600

        # Получаем размеры экрана
        screen_width = self.main_window.winfo_screenwidth()
        screen_height = self.main_window.winfo_screenheight()

        # Вычисляем координаты для центрирования
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        # Устанавливаем размеры и положение окна
        self.main_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Создать два виджета Lable
        self.label1 = tk.Label(self.main_window,text='Привет, мир!',
                               borderwidth = 1, relief= 'solid')
        self.label2 = tk.Label(self.main_window, text='sunken',
                               borderwidth = 4, relief= 'sunken')
        self.label3 = tk.Label(self.main_window, text='flat',
                               borderwidth=4, relief='flat')
        self.label4 = tk.Label(self.main_window, text='ridge',
                               borderwidth=4, relief='ridge')
        self.label5 = tk.Label(self.main_window, text='groove',
                               borderwidth=4, relief='groove')

        # Показать заголовок и вызвать метод pack виджетов Lebel, опеределение на листе и отсупы
        self.label1.pack(side='left', pady= 5) # side определение на листе
        self.label2.pack(side='top', pady= 5)
        self.label3.pack(side='left', pady= 5) # pady отступы
        self.label4.pack(side='top', pady= 5)
        self.label5.pack(side='left', pady= 5)
        # Вход в главный цикл tkinter
        tk.mainloop()
        # Создать экземпляр класса MyGUI
if __name__ =='__main__':
    my_gui = MyGUI()