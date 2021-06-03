def isaret(deger):
    if deger == 0: return '-'
    return '+' if deger >= 0 else ''


def deger_bul(deger, keys, values):
    for index, i in enumerate(keys):
        if i == deger:
            return values[index]
    return None


def cizgiyi_ciz(baslangic, bitis, h):
    cizgi_str = ''
    while baslangic <= bitis:
        cizgi_str += f'{round(baslangic, 5)}===='
        baslangic += h

    print(cizgi_str)
