class House():
    dafault_wall_material = "Кирпич" # атрибут класса

    def __init__(self, color, floors, sec_code): # __init__ автоматически запускается при создании объекта класса
        self.color = color
        self.floors = floors
        self.sec_code = sec_code
    def describe(self):
        print(f"Дом: {self.color}, Стены: {self.dafault_wall_material}, Этажей: {self.floors}, Код доступа: {self.sec_code}")

h1 = House("Белый", 1, 2333) # объект (экземпляр класса House)
h2 = House("Желтый", 2, 5555) # объект (экземпляр класса House)

h1.describe()
h2.describe()

#print(h1.dafault_wall_material)
# print(isinstance(h1,House)) # isinstance() позволяет проверять принадлежность объекта классу