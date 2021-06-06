from yaklasik_turev import *
from interpolasyon import *
from sayisal_integral import *
from diferansiyel_denklemler import *


def func(t, y):
    return t + y - 1


if __name__ == '__main__':
    #difaresiyel_euler(istenen_deger=1.2, h=0.1, verilen_nokta=(1, 0.5), func=func)
    #print('######################')
    difaresiyel_heun_duzeltilmis_euler(istenen_deger=2, h=0.5, verilen_nokta=(0, 2), func=func)
    #print('######################')
    #runge_kutta(istenen_deger=4, h=0.5, verilen_nokta=(0, 1), func=func)
