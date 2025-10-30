# Класс CellPhone содержит данные о сотовом телефоне

class CellPhone:
    # Метод __init__инициализирует АТРИБУТЫ
    def __init__(self, manufact, model, price):
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = price

    # Методы setters set_manufact, set_model,set_retail_price принимает аргумент для производителя телефона, модели и цены
    def set_manufact(self, manufact):
        self.__manufact = manufact

    def set_model(self, model):
        self.__model = model

    def set_retail_price(self, price):
        self.__retail_price = price
    # Методы getters get_manufact, get_model, get_retail_price возвращает аргумент аргумент для производителя телефона, модели и цены

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price