"""
    y' yalnız bırakılır, geri kalanlar karşı tarafa atılır.
    y' = f(t, y)
"""
import math

from utils import cizgiyi_ciz, deger_bul


def difaresiyel_euler(istenen_deger, aralik, h, *args):
    keys = []
    values = []

    for i in args:
        keys.append(i[0])
        values.append(i[1])

    if aralik is None:
        aralik = aralik_olustur(keys[0], istenen_deger)

    cizgiyi_ciz(aralik[0], aralik[1], h)

    deger = aralik[0]
    while aralik[1] > deger != istenen_deger:
        sonuc = round(deger_bul(deger, keys, values) + (h * func(deger, deger_bul(deger, keys, values))), 5)
        print(f'y({round(deger + h, 5)}) = y({round(deger, 5)}) + h*f[({round(deger, 5)}),'
              f'({round(deger_bul(deger, keys, values), 5)})] = {round(deger_bul(deger, keys, values), 5)} + '
              f'({h})*({round(func(deger, deger_bul(deger, keys, values)), 5)}) = {sonuc}')

        deger += h
        values.append(round(sonuc, 5))
        deger = round(deger, 5)
        keys.append(deger)


def difaresiyel_heun_duzeltilmis_euler(istenen_deger, aralik, h, *args):
    keys = []
    values = []

    for i in args:
        keys.append(i[0])
        values.append(i[1])

    if aralik is None:
        aralik = aralik_olustur(keys[0], istenen_deger)

    cizgiyi_ciz(aralik[0], aralik[1], h)
    deger = aralik[0]
    index = 1
    while aralik[1] > deger != istenen_deger:
        print(f'{index}. adım:')
        sonuc1 = round(deger_bul(deger, keys, values) + (h * func(deger, deger_bul(deger, keys, values))), 5)
        print(f'\ty^(1)({round(deger + h, 5)}) = y({round(deger, 5)}) + h*f[({round(deger, 5)}),'
              f'({round(deger_bul(deger, keys, values), 5)})] = {round(deger_bul(deger, keys, values), 5)} + '
              f'({h})*({round(func(deger, deger_bul(deger, keys, values)), 5)}) = {sonuc1}')

        sonuc2 = round(deger_bul(deger, keys, values) + (h * (func(deger, deger_bul(deger, keys, values)) +
                                                              func(deger + h, sonuc1))/2), 5)
        print(f'\ty^(2)({round(deger + h, 5)}) = y({round(deger, 5)}) + h*[(f[({round(deger, 5)}),'
              f'({round(deger_bul(deger, keys, values), 5)})]+f[({round(deger + h, 5)}),'
              f'({sonuc1})])/(2)] = {sonuc2}')

        deger += h
        index += 1
        values.append(round(sonuc2, 5))
        deger = round(deger, 5)
        keys.append(deger)


def runge_kutta(istenen_deger, aralik, h, *args):
    keys = []
    values = []

    for i in args:
        keys.append(i[0])
        values.append(i[1])

    if aralik is None:
        aralik = aralik_olustur(keys[0], istenen_deger)

    cizgiyi_ciz(aralik[0], aralik[1], h)
    deger = aralik[0]
    index = 1
    while aralik[1] > deger != istenen_deger:
        print(f'{index}. adım:')
        print(f'\ty({round(deger + h, 5)}) = y({deger}) + (h/2)*[F1 + F2]')
        F1 = round(func(deger, deger_bul(deger, keys, values)), 5)
        print(f'\tF1 = f({deger},{deger_bul(deger, keys, values)}) = {F1}')
        F2 = round(func(deger + h, deger_bul(deger, keys, values) + (h * F1)), 5)
        print(f'\tF2 = f[({deger} + {h}),({deger_bul(deger, keys, values)} + ({h} * {F1}))] = {F2}')
        sonuc = round(deger_bul(deger, keys, values) + ((h/2) * (F1 + F2)), 5)
        print(f'\ty({round(deger + h, 5)}) = {deger_bul(deger, keys, values)} + {round(h/2,5)} * ({F1} + {F2}) = {sonuc}')

        deger += h
        values.append(round(sonuc, 5))
        deger = round(deger, 5)
        keys.append(deger)
        index += 1


def aralik_olustur(baslangic, istenen_deger):
    return tuple((baslangic, istenen_deger))


def func(t, y):
    return (math.e**(-1 * t))/(1 + y)
