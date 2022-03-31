"""
Dana jest tablica T[N][N] wypełniona liczbami całkowitymi. Proszę napisać funkcję, która
wyszuka spójny podciąg elementów leżący poziomo lub pionowo o największej sumie. Maksymalna długość
podciągu może wynosić 10 elementów. Do funkcji należy przekazać tablicę T, funkcja powinna zwrócić sumę
maksymalnego podciągu.
"""


def cw17(t):
    if len(t) > 10:
        k = len(t) - 10
        max = 0
        result = [0]
        while k >= 0:
            print("k", k)
            for i in range(len(t)):
                print("i", i)
                for znacznik_1 in range(k, k + 10):
                    suma = 0
                    for x in range(znacznik_1, k + 10):
                        suma += t[i][x]
                        if suma > max:
                            max = suma
                            result[0] = t[i][znacznik_1:x + 1]
                        print(t[i][znacznik_1:x + 1])
                for znacznik_1 in range(k, k + 10):
                    suma = 0
                    for x in range(znacznik_1, k + 10):
                        suma += t[x][i]
                        if suma > max:
                            max = suma
                            result[0] = [t[znacznik_1][i] for znacznik_1 in range(znacznik_1, x + 1)]
            k -= 1

    else:
        znacznik_2 = len(t)
        max = 0
        result = [0]
        for i in range(len(t)):
            for znacznik_1 in range(znacznik_2):
                suma = 0
                for x in range(znacznik_1, znacznik_2):
                    suma += t[i][x]
                    if suma > max:
                        max = suma
                        result[0] = t[i][znacznik_1:x + 1]
            for znacznik_1 in range(znacznik_2):
                suma = 0
                for x in range(znacznik_1, znacznik_2):
                    suma += t[x][i]
                    if suma > max:
                        max = suma
                        result[0] = [t[znacznik_1][i] for znacznik_1 in range(znacznik_1, x + 1)]
                        print("result pionowy", result, suma)

    return max, result



print(cw17([[152, 33242, 45, 542, 66424, 675, 46, 76547, 4562, 3252, 13242],
            [124, 421, 3452, 523, 2342, 53453452, 52, 463, 235, 12346, 346],
            [23324, 443, 45321, 13224, 333, 552, 5231, 45, 235, 754, 235],
            [142, 123, 234, 1345, 55313, 23451, 73, 1, 2, 3, 4],
            [234, 5325, 23425, 412, 5524, 1341, 123, 352, 124, 7548, 325],
            [332, 512, 122, 421, 2341, 63467, 92, 413, 462, 46, 245],
            [22353, 45, 5521, 2324, 35351, 552412, 2, 64, 345, 324, 134],
            [412, 5624, 5346, 24572475, 725477, 54278, 346, 246, 2441, 64362, 45267],
            [54362, 243, 2646, 2457, 24, 57547, 634, 7868, 362211, 43515, 56],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            [23, 24, 25, 26, 27, 8, 9, 7 ,5, 4, 5]]))