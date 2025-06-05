MARK_UP = 2.5
another ='д'

while another == 'д' or another == 'Д':
    whosales = float(input("Введите оптовою стоимость товара: "))

    while whosales < 0:
        print("ОШИБКА: стоимость не может быть отрицательной.")
        whosales = float(input('Введите правильную ' +
                               'оптовую стоимость: '))
    retail = whosales * MARK_UP/100
    print(f'Розничная цена: ${retail:,.2f}')

    another = input('Есть еще один товар? ' +
                    '(Введите д, если да): ')
