import random
num_year = int(input("Введите количество лет, для определения слоя осадков: "))
num_month = int(input("Количество месяцев: "))

for year_loop in range(num_year):
    rain_line = 0
    print('Год', year_loop + 1)
    print('------------------')
    for month_loop in range(num_month):
        rain_line_random = random.randrange(30)
        rain_line += rain_line_random
        print(f'Номер месяца {month_loop},  {rain_line_random }', end='')
    rian_precipitation = rain_line * num_month
    print(f'{rain_line_random}, осадки мм.: {rain_line},средняя толщина дождевого слоя: {rian_precipitation}')
    print()