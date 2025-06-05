MAX = 5  # Максимальное число.
total = 0.0  # Накапливающая переменная

print('Эта программа вычисляет сумму из')
print(f'{MAX} чисел, которые вы введете.')

for counter in range(MAX):
    number = int(input('Введите число: '))
    total += number

print(f'Сумма составляет {total}.')
