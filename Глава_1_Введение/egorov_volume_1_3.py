age = float(input('Введите возраст для определения категории к которой относится человек: '))

if age <= 1 and age > 0:
    print('младенец')
elif age > 1 and age < 13:
    print('ребенок')
elif age >= 13 and age < 20:
    print('подросток')
elif age > 20:
    print('взрослый')
else:
    print('Нереальный возраст, введите данные еще раз!')