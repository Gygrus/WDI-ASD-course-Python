"""
Dana jest tablica int t[MAX][MAX]. Proszę napisać funkcję wypełniającą tablicę
liczbami naturalnymi po spirali.
"""

# def cw1(t):
#     i = 0
#     k = len(t[0]) - 1
#     z = len(t) - 1
#     wypisz = 1
#     print(len(t)*len(t[0]))
#     while True:
#
#         for x in range(i, k):
#             t[i][x] = wypisz
#             wypisz += 1
#
#
#         for x in range(i, z):
#             t[x][k] = wypisz
#             wypisz += 1
#
#
#         for x in range(k, i, -1):
#             t[z][x] = wypisz
#             wypisz += 1
#
#
#         for x in range(z, i, -1):
#             t[x][i] = wypisz
#             wypisz += 1
#
#         i += 1
#         k -= 1
#         z -= 1
#         if i == k:
#             t[i][k] = wypisz
#         print(i, k)
#         if wypisz - 1 == len(t)*len(t[0]) or wypisz == len(t)*len(t[0]):
#             break
#
#     return t


def cw1(t):
    i = 0
    k = len(t[0]) - 1
    wypisz = 1
    print(len(t)*len(t[0]))
    while True:
        for x in range(i, k):
            t[i][x] = wypisz
            t[x][k] = wypisz + k - i
            wypisz += 1

        wypisz += k - i
        for x in range(k, i, -1):
            t[k][x] = wypisz
            t[x][i] = wypisz + k - i
            wypisz += 1
        wypisz += k - i

        i += 1
        k -= 1
        if i == k:
            t[i][k] = wypisz

        if wypisz - 1 == len(t)**2 or wypisz == len(t)**2:
            break

    for x in t:
        print(x)
    return ''


print(cw1([[3, 65, 68, 47, 343, 1, 3],
           [66, 49, 9, 90, 586, 1, 3],
           [68, 54, 1, 60, 756, 1, 3],
           [47, 89, 38, 3, 322, 1, 3],
           [12, 522, 453, 2, 6, 1, 3],
           [1, 1, 1, 1, 1, 1, 2],
           [2, 4, 5, 6, 7, 3, 4]]))