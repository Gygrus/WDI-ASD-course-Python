"""
Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
zwraca liczbę par elementów, o określonym iloczynie, takich że elementy są odległe o jeden ruch skoczka
szachowego.
"""


def cw19(t, iloczyn):
    count = 0
    # tab = [0]**len(t)
    # a = 0
    for x in range(len(t)):
        for y in range(len(t)):
            if len(t) - y > 2 and len(t) - x > 1:           # w prawo i dół
                if t[x][y]*t[x+1][y+2] == iloczyn:
                    count += 1
            if y > 1 and len(t) - x > 1:                    # w lewo i dół
                if t[x][y]*t[x+1][y-2] == iloczyn:
                    count += 1
            if len(t) - y > 1 and len(t) - x > 2:           # w dół i prawo
                if t[x][y]*t[x+2][y+1] == iloczyn:
                    count += 1
            if y > 0 and len(t) - x > 2:                    # w dół i lewo
                if t[x][y]*t[x+2][y-1] == iloczyn:
                    count += 1
            if len(t) - y > 2 and x > 0:                    # w prawo i górę
                if t[x][y]*t[x-1][y+2] == iloczyn:
                    count += 1
            if y > 1 and x > 0:                             # w lewo i górę
                if t[x][y]*t[x-1][y-2] == iloczyn:
                    count += 1
            if len(t) - y > 1 and x > 1:                    # w górę i prawo
                if t[x][y]*t[x-2][y+1] == iloczyn:
                    count += 1
            if y > 0 and x > 1:                             # w górę i lewo
                if t[x][y]*t[x-2][y-1] == iloczyn:
                    count += 1

    return count/2



print(cw19([[1, 6, 34, 0, 3],
           [2, 2, 2, 2, 2],
           [0, 7, 53, 122, 0],
           [234, 4454, 78, 5125, 8697],
           [1, 0, 0, 231, 7]], 678))