"""
Liczby naturalne a,b są komplementarne jeżeli ich suma jest liczbą pierwszą. Dana
jest tablica typu int t[MAX][MAX] wypełniona liczbami naturalnymi. Proszę
napisać funkcję, która zeruje elementy nie posiadające liczby komplementarnej.
"""
from math import ceil, sqrt


def cw13(t):
    new = [0]*len(t)**2
    new_count = 0
    for x in range(len(t)):
        for y in range(len(t)):
            czy_komp = False
            if t[x][y] not in new and t[x][y] != 0:
                for i in range(len(t)):
                    for o in range(len(t)):
                        if t[i][o] != t[x][y] and t[i][o] != 0:
                            a = t[i][o] + t[x][y]
                            z = True
                            for k in range(2, ceil(sqrt(a)) + 1):
                                if a % k == 0:
                                    z = False
                            if z:
                                print("Udało się!", t[x][y], t[i][o])
                                czy_komp = True
                                new[new_count] = t[i][o]
                                new[new_count+1] = t[x][y]
                                new_count += 2
                                break
                    if z:
                        break

                if not(czy_komp):
                    t[x][y] = 0

    for x in t:
        print(x)



print(cw13([[1, 1, 3, 3, 3, 675],
           [7, 1, 6, 3, 3, 53452],
           [3, 3, 11, 3, 33, 5646],
           [1, 3, 1, 12, 1, 23451],
           [1, 3, 3, 3, 7, 1341],
           [32, 512, 122, 421, 2341, 63467]]))