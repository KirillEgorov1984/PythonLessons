from pydoc import describe


def main():
    # Открываем файл на чтение
    coffee_file = open('coffee.txt', 'r', encoding='utf-8')
    # прочитать поле с описанием первой записи
    descr = coffee_file.readline()
    # прочитать все отсальные записи

    while descr != '':
        qty = float(coffee_file.readline())
        descr= descr.rstrip('\n')

        print(f'Описание: {descr}')
        print(f'Количество: {qty}')

        descr = coffee_file.readline()

    coffee_file.close()

if __name__ == '__main__':
    main()

