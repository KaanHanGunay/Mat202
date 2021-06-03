from yaklasik_turev import *
from interpolasyon import *
from sayisal_integral import *
from diferansiyel_denklemler import *

if __name__ == '__main__':
    difaresiyel_euler(0.1, None, 0.1, (0, 1))
    print('######################')
    difaresiyel_heun_duzeltilmis_euler(0.1, None, 0.1, (0, 1))
    print('######################')
    runge_kutta(0.1, None, 0.1, (0, 1))
