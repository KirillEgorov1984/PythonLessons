import random
year = int(input("Введите количество лет, для определения слоя осадков: "))
MONTHS = 12

for year_loop in range(year):
    rain_line = 0
    for month_loop in range(MONTHS):
        rain_line += random.randint(5, 30)

    rian_precipitation = rain_line * MONTHS
    print(f'Количество месяцев: {MONTHS}, осадки мм.: {rain_line},средняя толщина дождевого слоя: {rian_precipitation}')
    print()