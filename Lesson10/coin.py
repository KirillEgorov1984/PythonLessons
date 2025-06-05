import random

# Класс Coin имитирует монету, которую
# можно подбрасывать.

class Coin:

    # Метод init инициализирует
    # атрибут данных sideup значением 'Орел'.

    def __init__(self):
        self.sideup = 'Орел'

    # Метод toss генерирует случайное число
    # в диапазоне от О до 1. Если это число
    # равно О, то sideup получает значение 'Орел'.
    # В противном случае sideup получает значение 'Решка'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Орел'
        else:
            self.sideup = 'Решка'
    # Метод get sideup возвращает значение,
    # на которое ссылается sideup.

    def get_sidup(self):
        return self.sideup