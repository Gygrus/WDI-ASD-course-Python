"""
Napisać funkcję która dla tablicy typu int t[MAX][MAX], wypełnionej liczbami
całkowitymi, zwraca wartość true w przypadku, gdy w każdym wierszu i każdej
kolumnie występuje co najmniej jedno 0 oraz wartość false w przeciwnym
przypadku.
"""

def cw10(t):
    for x in t:
        k = True
        for i in x:
            if i == 0:
                k = False
        if k:
            return False

    for i in range(len(t)):
        a = True
        for p in range(len(t)):
            if t[p][i] == 0:
                a = False
        if a:
            return False

    return True



print(cw10([[1, 6, 34, 0, 3],
           [0, 4, 6, 839, 7],
           [0, 7, 53, 122, 0],
           [1, 4, 1, 0, 1],
           [1, 0, 0, 231, 7]]))