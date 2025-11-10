import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("339x400")
        self.root.resizable(False, False)

        # Строка для выражения
        self.expression = ""

        # Поле вывода
        self.entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10, pady=10)

        # Кнопки
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            tk.Button(root, text=text, width=5, height=2, font=("Arial", 16),
                      command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
            self.entry.delete(0, tk.END)
        elif char == "=":
            try:
                result = str(eval(self.expression))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
                self.expression = result  # чтобы можно было продолжать вычисления
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Ошибка")
                self.expression = ""
        else:
            self.expression += str(char)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
