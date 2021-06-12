def jacobi_esas(baslangic_noktasi, istenen_deger, func_for_x, func_for_y, func_for_z):
    x_degerleri = [baslangic_noktasi[0]]
    y_degerleri = [baslangic_noktasi[1]]
    z_degerleri = [baslangic_noktasi[2]]

    result_str = 'k\t\tx\t\ty\t\tz\t\t\n'
    index = 0
    while index < istenen_deger:
        x_degeri = round(func_for_x(y_degerleri[index], z_degerleri[index]), 5)
        x_degerleri.append(x_degeri)

        y_degeri = round(func_for_y(x_degerleri[index], z_degerleri[index]), 5)
        y_degerleri.append(y_degeri)

        z_degeri = round(func_for_z(x_degerleri[index], y_degerleri[index]), 5)
        z_degerleri.append(z_degeri)

        result_str += f'{index + 1}\t\t{x_degerleri[index + 1]}\t\t{y_degerleri[index + 1]}\t\t{z_degerleri[index + 1]}\n'

        index += 1

    print(result_str)


def jacobi(baslangic_noktasi, istenen_deger, matris, sonuclar):

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


        print(f'{buyuk_pozisyon} => (({sonuclar[index]}) + (-1 * {kucuk_degerler[0]} * x) + (-1 * {kucuk_degerler[1]} * y)) / {buyuk_deger}')

        fonksiyonlar[buyuk_pozisyon] = create_function(sonuclar[index], kucuk_degerler[0], kucuk_degerler[1], buyuk_deger)

    jacobi_esas(baslangic_noktasi=baslangic_noktasi, istenen_deger=istenen_deger, func_for_x=fonksiyonlar[0],
                func_for_y=fonksiyonlar[1], func_for_z=fonksiyonlar[2])


def create_function(a, b, c, d):
    def func(x, y):
        return (a + (-1 * b * x) + (-1 * c * y)) / d
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
