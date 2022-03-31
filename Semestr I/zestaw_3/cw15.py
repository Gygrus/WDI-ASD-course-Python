



"""
Dana jest duża tablica t. Proszę napisać funkcję, która zwraca informację czy w tablicy
zachodzi następujący warunek: „wszystkie elementy, których indeks jest elementem ciągu Fibonacciego są
liczbami złożonymi, a wśród pozostałych przynajmniej jedna jest liczbą pierwszą”
"""
from math import sqrt
t = []

def cw15(t):
    a = 1
    b = 1
    while a <= len(t) - 1:
        p = False
        for x in range(2, int(sqrt(t[a])) + 1):
            if t[a] % x == 0:
                p = True
                break
        if p == False:
            return False
        c = a + b
        b = a
        a = c
    for x in t:
        k = True
        for i in range(2, int(sqrt(x)) + 1):
            if x % i == 0:
                k = False
        if k:
            return True

    return False



print(cw15([4, 8, 9, 6, 10, 10, 11, 8, 8]))
