import tkinter as tk
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Создать виджет главного окна
        self.main_window = tk.Tk()
        self.my_button =tk.Button(self.main_window,
                                  text='Нажми меня!',
                                  command=self.do_something)
        self.my_button.pack()

        tk.mainloop()
    def do_something(self):
        tk.messagebox.showinfo('Реакция',
                                   'Благодарю, что нажали кнопку.')
if __name__ =='__main__':
    my_gui = MyGUI()