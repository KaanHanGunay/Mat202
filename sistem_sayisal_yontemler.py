def jacobi_esas(baslangic_noktasi, istenen_deger, fonksiyonlar, gauss=False):
    degerler = []

    for i in baslangic_noktasi:
        degerler.append([i])

    print('k\t\t', end='')
    for i in range(len(baslangic_noktasi)):
        print(f'x{i}\t\t\t', end='')
    print('')

    index = 0
    while index <= istenen_deger:

        print(index, '\t\t', end='')
        for i in range(len(fonksiyonlar)):
            if gauss:
                liste = index_disindaki_degerler_gauss(i, degerler)
            else:
                liste = index_disindaki_degerler(i, degerler, index)
            degerler[i].append(round(fonksiyonlar[i](liste), 5))

        for i in range(len(baslangic_noktasi)):
            print(f'{degerler[i][-1]}\t\t', end='')
        print('')
        index += 1


def index_disindaki_degerler(index, degerler, bulunulan_index):
    liste = []
    for i, deger in enumerate(degerler):
        if i != index:
            liste.append(deger[bulunulan_index])
    return liste


def index_disindaki_degerler_gauss(index, degerler):
    liste = []
    for i, deger in enumerate(degerler):
        if i != index:
            liste.append(deger[-1])
    return liste


def jacobi(baslangic_noktasi, istenen_deger, matris, sonuclar, gauss=False):
    duzeltme_secimleri = []
    for i in matris:
        duzeltme_secimleri.append(jacobi_duzeltmesi(satir=i))

    fonksiyonlar = []

    for i in range(len(matris[0])):
        fonksiyonlar.append(None)

    for index, satir in enumerate(duzeltme_secimleri):
        kucuk_degerler = []
        buyuk_pozisyon = -1
        for i, deger in enumerate(satir):
            if (deger):
                buyuk_deger = matris[index][i]
                buyuk_pozisyon = i
            else:
                kucuk_degerler.append(matris[index][i])

        print(f'x{buyuk_pozisyon + 1} => ', end='')
        fonksiyonlar[buyuk_pozisyon] = create_function(sonuclar[index], buyuk_deger, kucuk_degerler)

    jacobi_esas(baslangic_noktasi=baslangic_noktasi, istenen_deger=istenen_deger, fonksiyonlar=fonksiyonlar, gauss=gauss)


def create_function(sonuc, buyuk_deger, kucuk_degerler):
    func_str = f'({sonuc} + '
    for index, deger in enumerate(kucuk_degerler):
        func_str += f'(-1 * {deger} + x{index + 1}) + '

    func_str = func_str[:-2] + f') / {buyuk_deger}'
    print(func_str)

    def func(liste):
        s = sonuc
        for index, arg in enumerate(liste):
            d = -1 * kucuk_degerler[index] * arg
            s += d
        return s / buyuk_deger

    return func


def jacobi_duzeltmesi(satir):
    degerler = []
    for i, deger in enumerate(satir):
        degerler.append(karsilastir(satir, i))

    return degerler


def karsilastir(satir, index):
    toplam = 0
    for i, deger in enumerate(satir):
        if i != index:
            toplam += abs(deger)

    return abs(satir[index]) > toplam


def gauss_siedel(baslangic_noktasi, istenen_deger, matris, sonuclar):
    jacobi(baslangic_noktasi=baslangic_noktasi, istenen_deger=istenen_deger, matris=matris, sonuclar=sonuclar, gauss=True)
