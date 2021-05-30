def isaret(deger):
    if deger == 0: return '-'
    return '+' if deger >= 0 else ''


def deger_bul(deger, keys, values):
    for index, i in enumerate(keys):
        if i == deger:
            return values[index]
    return None
