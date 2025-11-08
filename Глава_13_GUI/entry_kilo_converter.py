import tkinter
import tkinter.messagebox


class KiloConverter:
    def __init__(self):
        # Создать главное окно
        self.main_window = tkinter.Tk()

        # Создать две рамки, чтобы сгруппировать виджеты
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Создать виджеты для верхней рамки
        self.prompt_label = tkinter.Label(self.top_frame,
                                          text='Введите расстояние в километрах: ')
        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)

        # Упаковать виджеты верхней рамки
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

        # Создать кнопки для нижней рамки
        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text='Преобразовать',
                                          command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Выйти',
                                          command=self.main_window.destroy)

        # Упаковать кнопки и рамки
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Запустить главный цикл
        tkinter.mainloop()

    def convert(self):
        try:
            kilo = float(self.kilo_entry.get())
            miles = kilo * 0.6214

            tkinter.messagebox.showinfo(
                'Результаты',
                f'{kilo} километров эквивалентно {miles:.2f} милям'
            )
        except ValueError:
            tkinter.messagebox.showerror('Ошибка', 'Введите числовое значение!')


if __name__ == '__main__':
    kilo_conv = KiloConverter()




