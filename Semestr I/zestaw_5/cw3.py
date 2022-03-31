"""
Na szachownicy o wymiarach 100 na 100 umieszczamy N hetmanów (N < 100). Położenie
hetmanów jest opisywane przez tablicę dane = [(w1, k1),(w2, k2),(w3, k3), ...(wN , kN )] Proszę napisać funkcję, która odpowiada na pytanie: czy żadne z dwa hetmany się nie szachują? Do funkcji należy przekazać
położenie hetmanów.
"""
from random import randint

def czy_szachuja(tab):
    pom_w = [-1]*len(tab)
    pom_k = [-1]*len(tab)
    i_w = 0
    i_k = 0
    for x in tab:
        if x[0] in pom_w:
            return "Szachują się"

        else:
            pom_w[i_w] = x[0]
            i_w += 1

        if x[1] in pom_k:
            return "Szachują się"

        else:
            pom_k[i_k] = x[1]
            i_k += 1

    for x in tab:
        for p in tab:
            if x != p:
                if abs(x[0] - p[0]) == abs(x[1] - p[1]):
                    return "Szachują się!!", x, p


tab = [(randint(0, 99), randint(0, 99)) for _ in range(10)]

print(czy_szachuja(tab))