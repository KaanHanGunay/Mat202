def aralik_yarilama_yontemi(func, bolzano_araligi, epsilon, degerler=None):
    epsilon = round(epsilon, 5)
    if degerler is not None:
        eksi = degerler[0]
        arti = degerler[1]
    else:
        eksi, arti = bolzano(func=func, aralik=bolzano_araligi)
    print(f'Seçilen aralık => [{eksi}, {arti}]')
    print(f'f({eksi}) = {round(func(eksi), 5)} < 0')
    print(f'f({arti}) = {round(func(arti), 5)} > 0')
    sonuclar = []
    kullanilan_degerler = []

    fark = True
    index = 1
    while fark:
        orta_nokta = round((eksi + arti) / 2, 5)
        kullanilan_degerler.append(orta_nokta)
        s = round(func(orta_nokta), 5)
        sonuclar.append(s)
        isaret = '>' if s > 0 else '<'
        print(
            f'(-)  {eksi} -{"x" if isaret == "<" else "-"}- {orta_nokta} -{"x" if isaret == ">" else "-"}- {arti}  (+)',
            end='\t\t\t')
        print(f'P({index}) = ({eksi} + {arti}) / 2 => f({orta_nokta}) = {s} {isaret} {orta_nokta}', end='')

        if index == 1:
            fark = True
            print('')
        else:
            f = round(abs(kullanilan_degerler[index - 1] - kullanilan_degerler[index - 2]), 5)
            fark = f > epsilon
            print(f' => {f} {">" if fark else "<"} {epsilon}')

        if s > 0:
            arti = orta_nokta
        else:
            eksi = orta_nokta

        index += 1


def newton_raphson(func, func_turev, func_ikinci_turev, epsilon, bolzano_araligi):
    epsilon = round(epsilon, 5)
    eksi, arti = bolzano(func=func, aralik=bolzano_araligi)
    print(f'Seçilen aralık => [{eksi}, {arti}]')

    kontrol = False
    denenecek_sayi = eksi
    while not kontrol and denenecek_sayi < arti:
        kontrol = newton_raphson_kontrol(func, func_turev, func_ikinci_turev, denenecek_sayi)
        if not kontrol:
            denenecek_sayi += 0.1
        denenecek_sayi = round(denenecek_sayi, 5)

    if not kontrol:
        raise Exception('Bu değer kullanılamaz')

    sonuclar = [denenecek_sayi]

    index = 0
    fark = True

    while fark:
        s = sonuclar[index]
        func_s = round(func(s), 5)
        func_s_turev = round(func_turev(s), 5)
        sonuc = round(s - (func_s / func_s_turev), 5)
        print(f'x{index + 1} = {s} - (f({s})/f\'({s})) = {s} - ({func_s} / {func_s_turev}) = {sonuc}', end='')
        sonuclar.append(sonuc)

        if index == 1:
            fark = True
            print(f' => {round(abs(sonuc - s), 5)} > {epsilon}')
        else:
            f = round(abs(sonuc - s), 5)
            fark = f > epsilon
            print(f' => {f} {">" if fark else "<"} {epsilon}')

        index += 1


def newton_raphson_kontrol(func, func_turev, func_ikinci_turev, deger):
    func_res = round(func(deger), 5)
    func_turev_res = round(func_turev(deger), 5)
    func_ikinci_turev_res = round(func_ikinci_turev(deger), 5)
    sonuc = round(abs((func_ikinci_turev_res * func_res) / (func_turev_res ** 2)), 5)

    result = sonuc < 1

    if result:
        print(f'|(f\'\'({deger}) * f({deger}))/[f\'({deger})]^2| = '
              f'|({func_ikinci_turev_res} * {func_res})/{func_turev_res}^2| = {sonuc}')
        print(f'{sonuc} {"<" if sonuc < 1 else ">"} 1')
    else:
        print(f'{deger} kullanılamaz.')

    return result


def bolzano(func, aralik):
    eksi = None
    arti = None

    if aralik is None:
        aralik = (0, 10)

    for i in range(aralik[0], aralik[1]):
        if func(i) < 0 and eksi is None:
            eksi = i
        elif func(i) > 0 and arti is None:
            arti = i

        if eksi is not None and arti is not None:
            break

    return eksi, arti

