"""
Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Proszę napisać funkcję która
odpowiada na pytanie, czy w tablicy każdy wiersz zawiera co najmniej jedną liczbą złożoną wyłącznie z cyfr
będących liczbami pierwszymi?
"""
from math import sqrt

def cw16(t):
    for x in t:
        czy_z_pierwszych = True
        for i in x:
            k = i
            same_pierwsze = True
            while i != 0:
                z = i % 10
                if z == 0 or z == 1:
                    same_pierwsze = False
                    break

                else:
                    for d in range(2, int(sqrt(z)) + 1):
                        if z % d == 0:
                            same_pierwsze = False
                            break
                i = i // 10
            if same_pierwsze:
                print(k)
                break

        if not same_pierwsze:
            return False

    return True




print(cw16([[1, 6, 77, 212, 3],
           [2, 2, 2, 2, 2],
           [324, 738, 543, 122, 23],
           [234, 4454, 78, 5325, 8697],
           [1, 263, 46, 231, 97]]))