score = int(input('Значение переменной score:'))

А_score = 10
В_score = 20
С_score = 30
D_score = 40

if score >= А_score and score <= В_score:
    print ('Ваш уровень - А. ')
else:
    if score >= В_score and score <= С_score:
        print ('Ваш уровень - В. ')
    else:
        if score >= С_score and score <= D_score:
            print ('Ваш уровень - С.')
        else:
            if score >= D_score:
                print ('Ваш уровень - D. ')
            else:
                print ('Ваш уровень - F. ')