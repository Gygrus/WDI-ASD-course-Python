""""
Napisać funkcję, która dla N-elementowej tablicy t wypełnionej
liczbami naturalnym wyznacza długość najdłuższego,
spójnego podciągu geometrycznego.
"""

N = int(input("> "))


def geo(t):
    if len(t) == 1:
        return 1
    q = 0
    tab = []
    count = 0
    k = True
    maximum = 0
    for x in t:
        count += 1
        if k:
            q = t[1] / x
            tab.append(x)
            k = False
        else:
            if x / tab[-1] != q:
                if count - 1 > maximum:
                    maximum = count - 1
                    winning = tab[-maximum::]
                q = x / tab[-1]
                count = 2
        tab.append(x)
        if count > maximum:
            maximum = count
            winning = tab[-maximum::]
    return maximum, winning


print(geo([1, 9]))

