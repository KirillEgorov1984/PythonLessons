def main():
    first_name = input('Введите свое имя: ')
    last_name = input('Введите свою фамилию: ')
    print('Ваше имя в обратном порядке')
    revers_name(first_name, last_name)

def revers_name(first, last):
    print(last, first)

main()