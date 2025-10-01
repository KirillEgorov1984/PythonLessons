class BankAccount:

# Метод __init__ Принимает аргумент с остатком на счете. Присваевается атрибуту __balance
    def __init__(self, bal):
        self.__balance = bal
# Метод deposit вносит на счет вклад
    def deposit(self, amount):
        self.__balance += amount
# Метод withdraw снимает сумму со счета
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Ошибка: недостаточно средств')
    def get_balance(self):
        return self.__balance
    
