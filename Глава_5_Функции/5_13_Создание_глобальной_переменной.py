my_value =10

def show_value():
    print(my_value)
show_value()


# Пример объявления глобальной переменной
number = 0

def main():
    global number
    number = int(input('Введите число: '))
    show_number()

def show_number():
    print(f'Вы ввели число {number}')

main()

###