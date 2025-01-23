mon = 1
tue = 2
we = 3
thu = 4
fri = 5
sat = 6
sun = 7

month = int(input('Введите число от 1 до 7: '))

if month == mon:
    print('1 - понедельник')
elif month == tue:
    print('2 - вторник')
elif month == we:
    print('3 - среда')
elif month == thu:
    print('4 - четверг')
elif month == fri:
    print('5 - пятница')
elif month == sat:
    print('6 - суббота')
elif month == sun:
    print('7 - воскресенье')
else:
    print('Введенное число не входит в диапазон от 1 до 7. Введите корректную цифру !!!!')