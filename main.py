import math

from yaklasik_turev import *
from interpolasyon import *
from sayisal_integral import *
from diferansiyel_denklemler import *
from sistem_sayisal_yontemler import *
from yaklasik_deger_bulma import *


def sayisal_integral_fonksiyonu(x):
    return x ** 5


def diferansiyel_denklemler_fonksiyonu(t, y):
    return (math.sin(t) - (5 * y ** 2)) / 3


def yakalsik_deger_bulma_fonksiyonu(x):
    return (x ** 2) - math.sin(x) - 1


def yakalsik_deger_bulma_fonksiyonu_turev(x):
    return (2 * x) - math.cos(x)


def yakalsik_deger_bulma_fonksiyonu_ikinci_turev(x):
    return math.sin(x) + 2


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

    # Sistem Sayısal Yöntemler
    # Jacobi Yöntemi
    jacobi(baslangic_noktasi=(2, -1, 1), istenen_deger=7, matris=[[15, 5, -5], [5, 20, 10], [-5, 5, 15]],
           sonuclar=[29, -3, -7])
    print('#############################################')
    
    # Gauss-Siedel Yöntemler
    gauss_siedel(baslangic_noktasi=(2, -1, 1), istenen_deger=7, matris=[[15, 5, -5], [5, 20, 10], [-5, 5, 15]],
                 sonuclar=[29, -3, -7])
    print('#############################################')
    
    # Yaklaşık Deger Bulma
    # Aralık Yarılama
    epsilon = 3 * (10 ** -4)
    aralik_yarilama_yontemi(func=yakalsik_deger_bulma_fonksiyonu, bolzano_araligi=None, epsilon=epsilon)
    print('#############################################')
    
    epsilon = 3 * (10 ** -4)
    newton_raphson(func=yakalsik_deger_bulma_fonksiyonu, func_turev=yakalsik_deger_bulma_fonksiyonu_turev,
                   func_ikinci_turev=yakalsik_deger_bulma_fonksiyonu_ikinci_turev, epsilon=epsilon, bolzano_araligi=None)
    print('#############################################')
    """
    epsilon = 1 * (10 ** -4)
    newton_raphson(func=yakalsik_deger_bulma_fonksiyonu, func_turev=yakalsik_deger_bulma_fonksiyonu_turev,
                   func_ikinci_turev=yakalsik_deger_bulma_fonksiyonu_ikinci_turev, epsilon=epsilon,
                   bolzano_araligi=None)
    print('########################################### ##')
