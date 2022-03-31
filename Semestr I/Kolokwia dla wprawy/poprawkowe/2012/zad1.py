"""
Mamy tablicę [1..max,1..max] of integer. Wyzeruj w niej wszystkie liczby które nie mają w tablicy innej
liczby, która powstałaby poprzez przestawienie jej cyfr. (uważając na 1000 i 0100 - nie dziala).
"""

def get_numbers(n):
    copy = n
    counter = 0
    while copy != 0:
        copy //= 10
        counter += 1

    copy = n
    x = [0]*counter
    i = 0
    while copy != 0:
        z = copy % 10
        x[i] = z
        copy //= 10
        i += 1

    new = [0]*counter
    for t in x:
        p = t
        i = counter-1
        while i >= 0:
            if new[i] < p:
                k = new[i]
                new[i] = p
                p = k
            i -= 1
    print(x, new, n)
    return new


def zeruj(t):
    for x in range(len(t)):
        for y in range(x+1, len(t)):
            z = get_numbers(t[y])
            p = get_numbers(t[x])
            if p == z:
                t[x] = 0
                t[y] = 0

    return t

print(zeruj([5, 3, 6, 34, 23, 7 ,45 ,346, 436, 12, 532, 7, 32]))

print(get_numbers(34))