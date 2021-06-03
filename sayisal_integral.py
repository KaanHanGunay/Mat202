import math

from utils import isaret, cizgiyi_ciz


def sayisal_integral_dikdortgen(baslangic, bitis, h):
    result = 0
    index = 0
    while baslangic <= (bitis - h):
        func_res = round((h * func(baslangic)), 5)
        print(f'S{index} = (x{index + 1}-x{index}) * f(x{index}) = {h} * {func_res} = {h * func_res}')
        result += (h * func_res)
        baslangic += h
        index += 1

    result = round(result, 5)
    print(f'Sonuç = {result}')


def sayisal_integral_yamuk(baslangic, bitis, h):
    result = 0
    index = 0
    func_write = f'S ≈ {h / 2}['
    returning_values = []
    while baslangic <= bitis:
        carpan = 1 if index == 0 or baslangic == bitis else 2
        result += (carpan * func(baslangic))
        func_write += f'{"" if carpan == 1 else str(carpan)}f({round(baslangic, 5)})'
        returning_values.append(func(baslangic))

        if baslangic != bitis:
            func_write += ' + '

        baslangic += h
        index += 1

    func_write += f'] = {h/2}('
    result = round((h / 2 * result), 5)

    for index, val in enumerate(returning_values):
        if index == 0 or index == (len(returning_values) - 1):
            func_write += str(round(val, 5))
        else:
            func_write += f'2({round(val, 5)})'

        if not index == (len(returning_values) - 1):
            func_write += ' + '
        else:
            func_write += f') = {result}'

    print(func_write)


def simpson(baslanbic, bitis, nokta_sayisi):
    h = (bitis - baslanbic) / (nokta_sayisi - 1)
    print('h değeri =>', round(h, 5))
    cizgiyi_ciz(baslanbic, bitis, h)

    if nokta_sayisi % 2 == 1:
        simpson_tek(h, baslanbic, bitis)
    else:
        simpson_cift(h, baslanbic, bitis)


def simpson_tek(h, baslangic, bitis):
    print('Simpson 1/3 kuralı')
    ilk_katsayi = round((h / 3), 5)
    result_str = f' = {ilk_katsayi}('
    func_write = f'Integral f(x) dx = h/3('
    index = 0
    toplam = 0

    while baslangic <= bitis:
        if index == 0 or baslangic == bitis:
            func_write += f'f(x{index})'
            toplam += round(func(baslangic), 5)
            result_str += f'({round(func(baslangic), 5)})'
        elif index % 2 == 1:
            func_write += f'4f(x{index})'
            toplam += round((4 * func(baslangic)), 5)
            result_str += f'4 * ({round(func(baslangic), 5)})'
        else:
            func_write += f'2f(x{index})'
            toplam += round((2 * func(baslangic)), 5)
            result_str += f'2 * ({round(func(baslangic), 5)})'

        if baslangic != bitis:
            func_write += ' + '
            result_str += ' + '
        else:
            func_write += ')'
            result_str += ')'

        index += 1
        baslangic += h

    toplam = round(toplam * ilk_katsayi, 5)
    print(func_write + result_str, '=', toplam)


def simpson_cift(h, baslangic, bitis):
    print('Simpson 3/8 kuralı')
    ilk_katsayi = round((3 * h / 8), 5)
    result_str = f' = {ilk_katsayi}('
    func_write = f'Integral f(x) dx = 3h/8('
    index = 0
    toplam = 0

    while baslangic <= bitis:
        if index == 0 or baslangic == bitis:
            func_write += f'f(x{index})'
            toplam += round(func(baslangic), 5)
            result_str += f'({round(func(baslangic), 5)})'
        else:
            func_write += f'3f(x{index})'
            toplam += round((3 * func(baslangic)), 5)
            result_str += f'3 * ({round(func(baslangic), 5)})'

        if baslangic != bitis:
            func_write += ' + '
            result_str += ' + '
        else:
            func_write += ')'
            result_str += ')'

        index += 1
        baslangic += h

    toplam = round(toplam * ilk_katsayi, 5)
    print(func_write + result_str, '=', toplam)


def func(deger):
    return deger**5
