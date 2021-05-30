from utils import isaret


def lineer_iterpolasyon(a_noktasi, b_noktasi, istenen_deger):
    egim = (b_noktasi[1] - a_noktasi[1]) / (b_noktasi[0] - a_noktasi[0])
    print(f'm = {egim}')
    print(f'y = {a_noktasi[1]} {isaret(egim)} {egim}*(x {"+" if a_noktasi[0] < 0 else "-"} {a_noktasi[0]})')
    sonuc = egim * (istenen_deger - a_noktasi[0]) + a_noktasi[1]
    print(f'f({istenen_deger}) ≈ p ({istenen_deger}) = {sonuc}')
    return sonuc


def kuadratik_interpolasyon(a_noktasi, b_noktasi, c_noktasi, istenen_deger):
    print(f'p(x) = '
          f'{a_noktasi[1]} + (({b_noktasi[1]} - {a_noktasi[1]})/({b_noktasi[0]} - {a_noktasi[0]})) * '
          f'(x - {a_noktasi[0]}) + ['
          f'(({c_noktasi[1]} - {a_noktasi[1]})/(({c_noktasi[0]} - {a_noktasi[0]}) * ({c_noktasi[0]} - {b_noktasi[0]})))'
          f' - (({b_noktasi[1]} - {a_noktasi[1]})/(({b_noktasi[0]} - {a_noktasi[0]}) * ({c_noktasi[0]} - {b_noktasi[0]}'
          f')))]'
          f'(x - {a_noktasi[0]})(x - {b_noktasi[0]})')

    sonuc = \
        a_noktasi[1] + \
        ((b_noktasi[1] - a_noktasi[1]) / (b_noktasi[0] - a_noktasi[0]) * (istenen_deger - a_noktasi[0])) + \
        (((c_noktasi[1] - a_noktasi[1]) / (c_noktasi[0] - a_noktasi[0]) * (c_noktasi[0] - b_noktasi[0])) -
         ((b_noktasi[1] - a_noktasi[1]) / (b_noktasi[0] - a_noktasi[0]) * (c_noktasi[0] - b_noktasi[0]))) * \
        (istenen_deger - a_noktasi[0]) * (istenen_deger - b_noktasi[0])

    print(f'f({istenen_deger}) ≈ p ({istenen_deger}) = {sonuc}')
    return sonuc


def bolunmus_farklar(istenen_deger, *args):
    keys = []
    values = [[]]

    for i in args:
        keys.append(i[0])
        values[0].append(i[1])

    for i in range(1, len(keys)):
        gonderilecek_liste = values[len(values) - 1]
        values.append(yan_listeden_al(keys, gonderilecek_liste, i))

    for i in range(len(keys)):
        print('{0: >6}'.format(keys[i]), '\t', end='')
        for index, j in enumerate(values):
            if i >= index:
                print('{0: >6}'.format(round(j[i - index], 5)), '\t', end='')
        print('\n', end='')

    sonuc = 0
    fonksiyon = 'p(x) = '
    for index, i in enumerate(values):
        katsayi = values[index][0]
        fonksiyon = fonksiyon + f'({round(values[index][0], 5)})'

        carpan = 1
        if index > 0:
            count = index - 1
            while count >= 0:
                deger = -1 * keys[count]
                carpan = carpan * (istenen_deger + deger)
                fonksiyon = fonksiyon + f'(x{isaret(deger)}{deger})'
                count = count - 1
        fonksiyon = fonksiyon + ' + '

        sonuc = sonuc + (katsayi * carpan)
    print(fonksiyon[0:-2])
    sonuc = round(sonuc, 5)
    print(f'f({istenen_deger}) ≈ p ({istenen_deger}) = {sonuc}')


def yan_listeden_al(keys, liste, sayi):
    l = []

    fark = len(keys) - len(liste)

    for i in range(sayi, len(keys)):
        a = liste[i - fark] - liste[i - sayi]
        b = keys[i] - keys[i - sayi]
        c = a / b
        l.append(c)

    return l


def langrange_interpolasyonu(istenen_deger, *args):
    keys = []
    values = []

    for i in args:
        keys.append(i[0])
        values.append(i[1])

    fonk = 'p(x) = '
    for i in range(len(values)):
        fonk = fonk + f'{isaret(values[i])}{values[i]}' + langrange_bul(i, keys)

    sonuc = 0
    for i in range(len(values)):
        sonuc = sonuc + (values[i] * langrange_hesapla(i, keys, istenen_deger))

    sonuc = round(sonuc, 5)

    print(fonk)
    print(f'f({istenen_deger}) ≈ p ({istenen_deger}) = {sonuc}')


def langrange_bul(sira, keys):
    fonk = '('

    for index, i in enumerate(keys):
        if sira != index:
            fonk = fonk + f'(x{isaret(-1 * i)}{-1 * i})'

    fonk = fonk + '/'
    for index, i in enumerate(keys):
        if sira != index:
            fonk = fonk + f'({keys[sira]}{isaret(-1 * i)}{-1 * i})'

    fonk = fonk + ')'

    print(f'L{sira} = {fonk}')

    return fonk


def langrange_hesapla(sira, keys, x):
    pay = 1
    payda = 1
    for index, i in enumerate(keys):
        if sira != index:
            pay = pay * (x - i)

    for index, i in enumerate(keys):
        if sira != index:
            payda = payda * (keys[sira] - i)

    return pay / payda
