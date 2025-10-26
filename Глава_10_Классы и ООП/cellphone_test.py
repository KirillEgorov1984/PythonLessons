import cellphone

def main():
    # Получение данных о телефоне
    man = input('Введите производителя: ')
    mod = input('Введите номер модели: ')
    retail = float(input('Введите розничную цену: '))

    # Создание экземпляра класса CellPhone
    phone = cellphone.CellPhone(man, mod, retail)

    # Показать введенные данные

    print(f'Вот введенные Вами данные: ')
    print(f'Производитель: {phone.get_manufact()}')
    print(f'Номер модели: {phone.get_model()}')
    print(f'Розничная цена: ${phone.get_retail_price():,.2f} ')

# Вызов главной функции
if __name__ == '__main__':
    main()

