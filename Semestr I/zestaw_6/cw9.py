"""
Poprzednie zadanie. Program powinien wypisywać wybrane odważniki.
"""

def czy_mozliwe(T, masa, i, tab1, tab2, mode):
    tab1 = tab1[:]
    tab2 = tab2[:]
    if sum(tab1) == sum(tab2) + masa:
        return True
    if i == len(T):
        return False

    else:
        if mode == 0:
            tab1.append(T[i])
        if mode == 1:
            tab2.append(T[i])


        return czy_mozliwe(T, masa, i +1, tab1, tab2, 0) or czy_mozliwe(T, masa, i+1, tab1, tab2, 1) or czy_mozliwe(T, masa, i+1, tab1, tab2, 2)

def rek(T, masa):
    tab1 = list()
    tab2 = list()
    i = 0
    return czy_mozliwe(T, masa, i, tab1, tab2, 0)

print(rek([1, 3, 5, 10, 16, 24], 48))