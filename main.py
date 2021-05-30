from yaklasik_turev import *
from interpolasyon import *
from sayisal_integral import *

if __name__ == '__main__':
    # bolunmus_farklar(2, (0, 1), (1, 2), (3, 6), (5, 7))
    # print('################################')
    # langrange_interpolasyonu(2, (0, 1), (1, 2), (3, 6), (5, 7))
    # print('################################')
    # sayisal_turev(5, (1, 0), (3, 24), (5, 72), (7, 144))
    # print('################################')
    # sayisal_integral_yamuk(0, 0.8, 0.001)
    sayisal_integral_yamuk(0, 1, 0.2)
    print('################################')
    simpson(0, 1, 6)