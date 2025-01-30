import random

days = int(input("Введите количество дней: "))
mistakes = 0

for day in range(days):
    mistakes += random.randint(1,5)
print(f'За {days} количество ошибок составляет {mistakes: <5}')
