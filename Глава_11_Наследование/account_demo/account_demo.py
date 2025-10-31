import accounts

def main():
    print('Введите данные о сберегательном счете.')
    act_num = input('Номер счета: ')
    int_rate = float(input('Процентная ставка: '))
    balance = float(input('Остаток: '))

    savings = accounts.SavingAccount(act_num, int_rate, balance)

