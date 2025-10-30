import cellphone
def main():
    #Получить список объектов CellPhone
    phones = make_list()
    print('Вот введенные Вами данные:')
    display_list(phones)

def make_list():
    phone_list =[]
    print('Введите данные о пяти телефонах.')
    for count in range(1, 6):
        print('Номер телефона ' + str(count) + ':')
        man = input('Введите производителя: ')
        mod = input('Введите номер модели: ')
        retail = float(input('Введите розничную цену: '))
        print()
    # Создание нового объекта  СellPhone в памяти
        phone = cellphone.CellPhone(man, mod, retail)
        phone_list.append(phone) #Добавление объекта в список

    return phone_list

# Функуия display_list принимает список с объектами СellPhone в качестве аргумента и показывает хранящиеся в каждом объекте данные

def display_list(phone_list):
    for item in phone_list:
        print(item.get_manufact())
        print(item.get_model())
        print(item.get_retail_price())
        print()

if __name__ == '__main__':
    main()