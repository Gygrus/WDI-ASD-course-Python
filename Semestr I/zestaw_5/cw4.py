"""
Dana jest tablica zawierająca liczby wymierne. Proszę napisać funkcję, która policzy występujące w tablicy ciągi arytmetyczne (LA) i geometryczne (LG) o długości większej niż 2. Funkcja powinna
zwrócić wartość 1 gdy LA > LG, wartość -1 gdy LA < LG oraz 0 gdy LA = LG.
"""
def skracanie(a):
    x = a[0]
    y = a[1]
    i = 2
    while i <= abs(max(x, y)):
        if x % i == 0 and y % i == 0:
            x //= i
            y //= i

        else:
            i += 1
    if y < 0 and x > 0:
        x = -x
        y = -y

    if y < 0 and x < 0:
        x = -x
        y = -y

    return (x, y)

def odejmowanie(a, b):
    if a[1] == b[1]:
        return skracanie((a[0] - b[0], a[1]))

    else:
        return skracanie((a[0] * b[1] - b[0] * a[1], a[1] * b[1]))

def dzielenie(a, b):
    return skracanie((a[0]*b[1], a[1]*b[0]))

# print(odejmowanie((6, 2), (6, 3)))
# print(odejmowanie((8, 2), (6, 2)))
# print(odejmowanie((9, 1), (8, 2)))
# print(odejmowanie((3, 2), (9, 1)))

from random import randint

def f(t):
    LA = 0
    LG = 0
    k = len(t)
    while k != 2:
        i = 0
        while k - 1 + i != len(t):
            r = odejmowanie(t[i+1], t[i])
            q = dzielenie(t[i+1], t[i])
            z_ar = True
            z_geo = True
            for x in range(i, k - 1 + i):
                if z_ar:
                    if odejmowanie(t[x+1], t[x]) != r:
                        z_ar = False
                if z_geo:
                    if dzielenie(t[x+1], t[x]) != q:
                        z_geo = False

            if z_ar:
                LA += 1
                
            if z_geo:
                LG += 1

            i += 1


        k -= 1


    if LA > LG:
        return 1, LA, LG
    elif LA < LG:
        return -1, LA, LG
    else:
        return 0, LA, LG



t = [(randint(0, 5), randint(1, 5)) for _ in range(100)]

print(t)
print(f(t))