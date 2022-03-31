"""
Dana jest tablica wypeªniona liczbami naturalnymi int t[N][N] reprezentuj¡ca szachownic¦. Prosz¦ napisa¢
funkcj¦, która sprawdza, czy jest mo»liwe ustawienie dwóch wzajemnie szachuj¡cych si¦ skoczków tak, aby
suma warto±ci pól, na których stoj¡ skoczki, byªa liczb¡ pierwsz¡. Do funkcji nale»y przekaza¢ tablic¦ t,
funkcja powinna zwróci¢ warto±¢ typu bool.
"""
from math import sqrt, ceil
from random import randint

def f(t):
    for x in range(len(t) - 1):
        for y in range(len(t)):
            sk_upper = t[x][y]
            for k in t[x+1]:
                check = k+sk_upper
                z = True
                for i in range(2, ceil(sqrt(check)) + 1):
                    if check % i == 0:
                        z = False
                        break
                if z:
                    if y < 2:
                        if k == t[x+1][y+2]:
                            return True, [x, y], k
                    elif y > len(t) - 3:
                        if k == t[x+1][x-2]:
                            return True, [x, y], k
                    else:
                        if k == t[x+1][y+2] or k == t[x+1][y-2]:
                            return True, [x, y], k

            if x < len(t) - 2:
                for k in t[x + 2]:
                    check = k + sk_upper
                    z = True
                    for i in range(2, ceil(sqrt(check)) + 1):
                        if check % i == 0:
                            z = False
                            break

                    if z:
                        if y < 1:
                            if k == t[x + 2][y + 1]:
                                return True, [x, y], k
                        elif y > len(t) - 2:
                            if k == t[x + 2][x - 1]:
                                return True, [x, y], k
                        else:
                            if k == t[x + 2][y + 1] or k == t[x + 2][y - 1]:
                                return True, [x, y], k



t = [0]*8
for i in range(len(t)):
    t[i] = [randint(1, 8) for _ in range(8)]
    print(t[i])


print(f(t))
