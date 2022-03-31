"""
Napisać funkcję, która dla N-elementowej tablicy t wypełnionej
liczbami naturalnym wyznacza długość najdłuższego,
spójnego podciągu arytmetycznego.
"""
"""
Używam pomocniczej listy tab, w której przechowuje poprzednie wartości ciągu w tablicy 
"""


def podc(t):
    count = 0
    i = 0
    maximum = 0
    tab = [0]
    r = t[0]
    for x in t:

        count += 1

        if x <= tab[-1]:

            if count - 1 > maximum:
                maximum = count - 1
            r = x - tab[-1]
            count = 1
        if x > tab[-1] and x - tab[-1] != r:
            if count - 1 > maximum:
                maximum = count - 1
            count = 2
            r = x - tab[-1]


        if count > maximum:
            maximum = count
        tab.append(x)



    return maximum


print(podc([2, 5, 1, 3, 5, 7, 9, 11, 13, 15, 5, 3, 2, 1, 2, 3, 4, 5, 6]))