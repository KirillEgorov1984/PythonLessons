def main():
    #Создаем булеву переменную
    found = False
    search = input('Введите искомое описание: ')
    # открыть файл
    coffee_file = open('coffee.txt', 'r')

    descr = coffee_file.readline() # полное описание по первой записи

    while descr !='':
        qty = float(coffee_file.readline())
        descr =descr.rstrip('\n')

        if descr == search:
            print(f'Описание: {descr}')
            print(f'Количество: {qty}')
            print()

            found = True
        descr = coffee_file.readline()

    coffee_file.close()

    if not found:
        print('Это значение в файле не найдено.')

  if __name__ == '__main__':
    main()

