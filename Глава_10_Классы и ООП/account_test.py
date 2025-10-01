import bankaccount

def main():
    start_bal = float(input('Введите свой начальный остаток: '))
    # Создается объект BankAccount
    savings = bankaccount.BankAccount(start_bal)

    pay = float(input('Сколько Вы получили на этой неделе? '))
    print('Вношу эту сумму на Ваш счет.')

    savings.deposit(pay)
    print(f'Ваш остаток на счете составляет ${savings.get_balance():,.2f}.')

    cash = float(input('Какую сумму Ві желаете снять со счета? '))
    print(f'Снимаю эту сумму с Вашего банковского счета.')

    savings.withdraw(cash)
    print(f'Ваш остаток на счете составляет ${savings.get_balance():,.2f}.')

if __name__ == '__main__':
    main()
