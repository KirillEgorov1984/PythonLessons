import vehicles

def main():
    car = vehicles.Car('BMW', 2001, 70000,15000.0,4)
    truck = vehicles.Truck('Toyota', 2002, 40000, 12000.0, '4WD')
    suv = vehicles.SUV('Volvo', 2000, 30000, 18500.0,5)

    print()
    print('==========================')
    print('ПОДЕРЖАННЫЕ АВТО НА СКЛАДЕ')
    print('==========================')

    print('Данный легковой автомобиль имеется на складе.')
    print('Изготовитель:', car.get_make())
    print('Модель:', car.get_model())
    print('Пробег:', car.get_mileage())
    print('Цена:', car.get_price())
    print('Количество дверей:', car.get_doors())
    print()

    print('Данный пикап имеется на складе.')
    print('Изготовитель:', truck.get_make())
    print('Модель:', truck.get_model())
    print('Пробег:', truck.get_mileage())
    print('Цена:',truck.get_price())
    print('Тип привода:', truck.get_drive_type())
    print()

    print('Данный джип имеется на складе.')
    print('Изготовитель:', suv.get_make())
    print('Модель:', suv.get_model())
    print('Пробег:', suv.get_mileage())
    print('Цена:', suv.get_price())
    print('Пассажирская вместимость:', suv.get_pass_cap())
    print()

if __name__ == '__main__':
    main()