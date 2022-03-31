"""
Problem skoczka szachowego. Proszę napisać funkcję, która wypełnia pola szachownicy o
wymiarach NxN ruchem skoczka szachowego.
"""


def fill(T, i, w, k, tab):
    print(w, k)
    T = list(map(list, T))
    tab = tab[:]
    tab.append((w, k))

    if i == len(T)**2:
        for x in T:
            print(x)
        return True, tab

    else:
        if w > len(T) - 1 or w < 0 or k > len(T) - 1 or k < 0 or T[w][k] == 1:
            return False
        else:
            T[w][k] = 1
            # print(tab)
            return fill(T, i + 1, w+2, k-1, tab) or fill(T, i + 1, w+2, k+1, tab) or fill(T, i + 1, w+1, k+2, tab) or fill(T, i + 1, w+1, k-2, tab) or fill(T, i + 1, w-1, k-2, tab) or fill(T, i + 1, w-1, k+2, tab) or fill(T, i + 1, w-2, k-1, tab) or fill(T, i + 1, w-2, k+1, tab)


def rek(T):
    i = 0
    w = 0
    k = 0
    tab = list()
    return fill(T, i, w, k, tab)

T = [[0 for _ in range(8)] for _ in range(8)]


print(rek(T))