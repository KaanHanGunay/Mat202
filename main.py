import math

from yaklasik_turev import *
from interpolasyon import *
from sayisal_integral import *
from diferansiyel_denklemler import *
from sistem_sayisal_yontemler import *


def sayisal_integral_fonksiyonu(x):
    return x ** 5


def diferansiyel_denklemler_fonksiyonu(t, y):
    return (math.sin(t) - (5 * y ** 2)) / 3


def func_for_x(y, z):
    result = round((15 - y - (5 * z)) / 2, 5)
    print(f'(15 - {y} - (5 * {z})) / 2 = {result}')
    return result


def func_for_y(x, z):
    result = round((-21 - (4 * x) - z) / (-8), 5)
    print(f'(-21 - (4 * {x}) - {z}) / (-8) = {result}')
    return result


def func_for_z(x, y):
    result = round(7 + y - (4 * x), 5)
    print(f'7 + {y} - (4 * {x}) = {result}')
    return result


if __name__ == '__main__':
    """
    # İnterpolasyon
    # Lineer İnterpolasyon
    lineer_iterpolasyon((2, 7), (3, 11), 7)
    print('#############################################')

    # Kuadratik İnterpolasyon
    kuadratik_interpolasyon((1, 5), (3, 1), (4, 0.5), 0)
    print('#############################################')

    # Bölünmüş Farklar
    bolunmus_farklar(0.5, (1, 5), (3, 1), (4, 0.5))
    print('#############################################')
    bolunmus_farklar(0, (1, -3), (2, 0), (3, 15))
    print('#############################################')
    bolunmus_farklar(0, (1, -3), (2, 0), (4, 48), (5, 105))
    print('#############################################')

    # Langrange İnterpolasyonu
    langrange_interpolasyonu(1, (2, 0.5), (2.5, 4), (4, 0.25))
    print('#############################################')
    langrange_interpolasyonu(0, (1, 5), (3, 1), (4, 0.5))
    print('#############################################')

    # Sayısal Türev
    sayisal_turev(1, (0.9, 2.4506), (1, 2.7182), (1.1, 3.0041))
    print('#############################################')

    # Sayısal İntegral
    # Dikdörtgen Yöntemi
    sayisal_integral_dikdortgen(baslangic=0, bitis=0.8, h=0.2, func=sayisal_integral_fonksiyonu)
    print('#############################################')

    # Yamuk Yöntemi
    sayisal_integral_yamuk(baslangic=0, bitis=0.8, h=0.2, func=sayisal_integral_fonksiyonu)
    print('#############################################')

    # Simpson Yöntemi
    simpson(baslangic=0, bitis=1, nokta_sayisi=5, func=sayisal_integral_fonksiyonu)
    print('#############################################')
    simpson(baslangic=0, bitis=1, nokta_sayisi=6, func=sayisal_integral_fonksiyonu)
    print('#############################################')

    # Diferansiyel Denklemler
    # Euler Yöntemi
    difaresiyel_euler(istenen_deger=0.4, h=0.2, verilen_nokta=(0, 5), func=diferansiyel_denklemler_fonksiyonu)
    print('#############################################')

    # Düzeltilmiş Euler (Heun) Yöntemi
    difaresiyel_heun_duzeltilmis_euler(istenen_deger=0.4, h=0.2, verilen_nokta=(0, 5), func=diferansiyel_denklemler_fonksiyonu)
    print('#############################################')

    # Runge Kutta Yöntemi
    runge_kutta(istenen_deger=0.9, h=0.3, verilen_nokta=(0.3, 5), func=diferansiyel_denklemler_fonksiyonu)
    print('#############################################')
    """

    jacobi(baslangic_noktasi=(0, 0, 0), istenen_deger=2, matris=[[20, 1, -2], [3, 20, -1], [2, -3, 20]], sonuclar=[17, -18, 25])
