length = float(input(f"Введите длину гряды в метрах:  "))
space = float(input(f"Размер пространства в метрах, занимаемого концевыми опорами:  "))
distance = float(input(f"Расстояние между виноградными лозами в метрах:  "))
quantity = int((length - 2 * space)//distance)

print(f"Количество виноградных лоз, которые поместяться на гряде {quantity:>10,.2f}")