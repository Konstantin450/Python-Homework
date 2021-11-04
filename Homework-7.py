def inch_sentemetre():
    x = int(input("Введите число: "))
    sent = x*2.54
    a = print(f"Дюймов {x} - {sent} сантиметров")
    return a


def sentemetre_inch():
    x = int(input("Введите число: "))
    inch = x*0.39
    a = print(f'Сантиметров {x} - Дюймов {inch}')
    return a


def mile_kilometrs():
    i = int(input("Введите число: "))
    km = i*1.6
    a = print(f'Миль {i} - Киллометров {km}')
    return a


def kilometres_mile():
    i = int(input("Введите число: "))
    mile = i*0.62
    a = print(f'Киллометров {i} - Миль {mile}')
    return a


def funt_kg():
    i = int(input("Введите число: "))
    kg = i*0.45
    a = print(f'Фунтов {i} - Килограмм {kg}')
    return a


def kg_funt():
    i = int(input("Введите число: "))
    funt = i*2.204
    a = print(f'Килограммы {i} - Фунты {funt}')
    return a


def unc_gramm():
    i = int(input("Введите число: "))
    gramm = i*28.35
    a = print(f'Унции {i} - Граммы {gramm}')
    return a


def gramm_unc():
    i = int(input("Введите число: "))
    unc = i*0.035
    a = print(f'Граммы {i} - Унции {unc}')
    return a


def gal_litr():
    i = int(input("Введите число: "))
    litr = i*4.55
    a = print(f'Галлоны {i} - Литры {litr}')
    return a


def litr_gal():
    i = int(input("Введите число: "))
    gal = i*0.22
    a = print(f'Литры {i} - Галлоны {gal}')
    return a


def pint_litr():
    i = int(input("Введите число: "))
    litr = i*0.57
    a = print(f'Пинты {i} - Литры {litr}')
    return a


def litr_pint():
    i = int(input("Введите число: "))
    pint = i*1.76
    a = print(f'Литры {i} - Пинты {pint}')
    return a


print('1.Дюймы в сантиметры')
print('2.Сантиметры в дюймы')
print('3.Мили в километры')
print('4.Километры в мили')
print('5.Фунты в килограммы')
print('6.Килограммы в фунты')
print('7.Унции в граммы')
print('8.Граммы в унции')
print('9.Галлон в литры')
print('10.Литры в галлоны')
print('11.Пинты в литры')
print('12.Литры в пинты')
while True:
    zapros = int(input("Введите цифру желаемой операции: "))
    if zapros == 1:
        inch_sentemetre()
    elif zapros == 2:
        sentemetre_inch()
    elif zapros == 3:
        mile_kilometrs()
    elif zapros == 4:
        kilometres_mile()
    elif zapros == 5:
        funt_kg()
    elif zapros == 6:
        kg_funt()
    elif zapros == 7:
        unc_gramm()
    elif zapros == 8:
        gramm_unc()
    elif zapros == 9:
        gal_litr()
    elif zapros == 10:
        litr_gal()
    elif zapros == 11:
        pint_litr()
    elif zapros == 12:
        litr_gal()
    elif zapros == 0:
        break
    else:
        print("Перепроверьте введенные данные!")
