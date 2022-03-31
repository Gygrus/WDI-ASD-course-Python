"""
”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład
waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool.
"""

def licz_wage(n):
    tab = []
    i = 2
    while n != 1:
        if n % i == 0:
            if i not in tab:
                tab.append(i)
            n //= i
        else:
            i += 1
    return len(tab)

def waga_wszystkich(T):
    suma = 0
    for x in T:
        suma += licz_wage(x)
    return suma

def sprawdz_podzb(tab1, tab2, tab3, index, mode, T):
    print(tab1, tab2, tab3)
    tab1 = tab1[:]
    tab2 = tab2[:]
    tab3 = tab3[:]
    if index >= len(T):
        if waga_wszystkich(tab1) == waga_wszystkich(tab2) and waga_wszystkich(tab2) == waga_wszystkich(tab3):
            return True
        else:
            return False
    else:
        if mode == 0:
            tab1.append(T[index])
        elif mode == 1:
            tab2.append(T[index])
        elif mode == 2:
            tab3.append(T[index])

    return sprawdz_podzb(tab1, tab2, tab3, index+1, 0, T) or sprawdz_podzb(tab1, tab2, tab3, index+1, 1, T) or sprawdz_podzb(tab1, tab2, tab3, index+1, 2, T)


def rek(T):
    tab1 = list()
    tab2 = list()
    tab3 = list()
    return sprawdz_podzb(tab1, tab2, tab3, 0, 0, T) or sprawdz_podzb(tab1, tab2, tab3, 0, 1, T) or sprawdz_podzb(tab1, tab2, tab3, 0, 2, T)


print(rek([2, 3, ]))