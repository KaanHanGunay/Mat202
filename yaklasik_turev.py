from utils import isaret, deger_bul


def sayisal_turev(istenen_deger, *args):
    keys = []
    values = []

    for i in args:
        keys.append(i[0])
        values.append(i[1])

    h = round(args[1][0] - args[0][0], 5)
    ileri_fark(h, istenen_deger, keys, values)
    geri_fark(h, istenen_deger, keys, values)
    merkezi_fark(h, istenen_deger, keys, values)
    ikinci_turev(h, istenen_deger, keys, values)


def ileri_fark(h, istenen_deger, keys, values):
    ileri_deger = deger_bul(istenen_deger + h, keys, values)
    tam_deger = deger_bul(istenen_deger, keys, values)
    sonuc = round((ileri_deger - tam_deger) / h, 5)

    print('İleri Fark => ', end='')
    print(f'f\'({istenen_deger})=(f({istenen_deger + h})-f({istenen_deger}))/h = ', end='')
    print(f'({ileri_deger}{isaret(-1 * tam_deger)}{-1 * tam_deger})/{h} = {sonuc}')

    return sonuc


def geri_fark(h, istenen_deger, keys, values):
    geri_deger = deger_bul(istenen_deger - h, keys, values)
    tam_deger = deger_bul(istenen_deger, keys, values)
    sonuc = round((tam_deger - geri_deger) / h, 5)

    print('Geri Fark => ', end='')
    print(f'f\'({istenen_deger})=(f({istenen_deger})-f({istenen_deger - h}))/h = ', end='')
    print(f'({tam_deger}{isaret(-1 * geri_deger)}{-1 * geri_deger})/{h} = {sonuc}')

    return sonuc


def merkezi_fark(h, istenen_deger, keys, values):
    geri_deger = deger_bul(istenen_deger - h, keys, values)
    ileri_deger = deger_bul(istenen_deger + h, keys, values)
    sonuc = round((ileri_deger - geri_deger) / (2 * h), 5)

    print('Merkezi Fark => ', end='')
    print(f'f\'({istenen_deger})=(f({istenen_deger + h})-f({istenen_deger - h}))/2h = ', end='')
    print(f'({ileri_deger}{isaret(-1 * geri_deger)}{-1 * geri_deger})/{2 * h} = {sonuc}')
    return sonuc


def ikinci_turev(h, istenen_deger, keys, values):
    ileri_deger = deger_bul(istenen_deger + h, keys, values)
    tam_deger = deger_bul(istenen_deger, keys, values)
    geri_deger = deger_bul(istenen_deger - h, keys, values)
    h2 = round(h**2, 5)
    sonuc = round((ileri_deger - (2 * tam_deger) + geri_deger) / h2, 5)

    print('İkinci türev => ', end='')
    print(f'f\'\'({istenen_deger})=(f({istenen_deger + h})-2f({istenen_deger})-f({istenen_deger - h}))/h² =', end='')
    print(f'({ileri_deger}){"-" if tam_deger < 0 else "+"}2*{tam_deger}{isaret(geri_deger)}{geri_deger})/{h2} = {sonuc}')

    return sonuc
