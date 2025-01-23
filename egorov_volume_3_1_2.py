length_one_rectangle = int(input('Введите длину первого прямоугольника: '))
width_one_rectangle = int(input('Введите ширину первого прямоугольника: '))
length_second_rectangle = int(input('Введите длину второго прямоугольника: '))
width_second_rectangle = int(input('Введите ширину второго прямоугольника: '))

square_rectangle_one = length_one_rectangle * width_one_rectangle
square_rectangle_second = length_second_rectangle * width_second_rectangle

if square_rectangle_one > square_rectangle_second:
    print(f'Площадь первого прямоугольника больше второго ! И равна : {square_rectangle_one}')
elif square_rectangle_one < square_rectangle_second:
    print(f'Площадь второго прямоугольника больше первого ! И равна : {square_rectangle_second}')
elif square_rectangle_one == square_rectangle_second:
    print(f'Площадь прямоугольников одинаковая! И равна  : {square_rectangle_second}')
else:
    print('Данные не определенны!!!!!!!')