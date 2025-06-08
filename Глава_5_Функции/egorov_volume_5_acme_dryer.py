def main():
    startup_massage()
    input('Нажмите Enter, чтобы увидеть шаг 1.')
    step1()
    input('Нажмите Enter, чтобы увидеть шаг 2.')
    step2()
    input('Нажмите Enter, чтобы увидеть шаг 3.')
    step3()
    input('Нажмите Enter, чтобы увидеть шаг 4.')
    step4()

def startup_massage():
    print('Эта программа дает рекомендации')
    print('по разборке бельевой сушилки фирмы ACME.')
    print('Данный процесс состоит из 4 шагов.')
    print()

def step1():
    print('Шаг 1: отключить сушилку и')
    print('отодвинуть ее от стены.')
    print()

def step2():
    print('Шаг 2: удалить шесть винтов')
    print('с задней стороны сушилки.')
    print()

def step3():
    print('Шаг 3: удалить заднюю панель')
    print('сушилки.')
    print()

def step4():
    print('Шаг 4: вынуть верхний блок')
    print('сушилки.')
    print()

main()



