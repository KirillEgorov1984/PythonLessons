# Программа добавляет записи о запасах кофе в файл coffee.txt

def main():
    # Создаем переменную для управления циклом
    another = 'д'
    # Открываем файл на дозапись
    coffee_file = open('coffee.txt', 'a', encoding='utf-8')

    # Добавляем запись в файл через цикл
    while another == 'д' or another == 'Д':
        print('Введите следующие данные о кофе.')
        descr = input('Описание: ')
        qty = int(input('Количество (в фунтах): '))
        
        # Добавить данные в файл
        coffee_file.write(f'{descr}\n')
        coffee_file.write(f'{qty}\n')

        # Вопрос к пользователю, хочет он добавить еще одну запись или нет
        print('Желаете ли Вы добавить еще одну запись?')
        another = input('Д = да, все остальное = нет: ')

    #Закрыть файл
    coffee_file.close()
    print('Данные добавлены в coffee.txt.')

if __name__ == '__main__':
    main()