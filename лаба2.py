def z1():
    a = input()
    b = input()
    if a == b:
        print ('Пароль принят')
    else:
        print ('Пароль не принят')

def z2():
    a = int(input())
    if a % 2 == 0:
        print ('Верхнее место')
    else:
        print('Нижнее место')
    if a<37:
        print('Купе')
    else:
        print('Боковое место')

def z3():
    a=int(input())
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        print ('Год a - високосный год')
    else
        print('Это год не високосный')

def z4():
    a = input()
    b = input()
    if a != 'красный' and a != 'желтый' and a != 'синий' or b != 'красный' and b != 'желтый' and b != 'синий':
        print ('Ошбика')
    elif a == 'красный' and b == 'желтый' or a == 'желтый' and b == 'красный':
        print ('Оранжевый')
    elif a == 'синий' and b == 'красный' or b == 'синий' and a == 'красный':
        print ('Фиолетовый')
    elif a == b:
        print (a)
    else:
        print('зеленый')