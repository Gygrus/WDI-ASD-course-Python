"""
Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami naturalnym wyznacza
długość najdłuższego, spójnego podciągu rosnącego.
"""

def length(t):
    count = 0
    i = 0
    maxim = 0
    new_t = []
    for x in t:
        i += 1
        count += 1
        new_t.append(x)
        if i == len(t):
            if x <= t[i-2]:

                if count > maxim:
                    maxim = count
                    result = new_t
                count = 0
                new_t = []
            elif x > t[i-2] and count > maxim:
                maxim = count
                result = new_t

            break
        if x >= t[i]:

            if count > maxim:
                maxim = count
                result = new_t
            count = 0
            new_t = []
    return maxim, result

print(length([2, 3, 5, 6, 7, 8, 3, 6, 5, 6, 7, 8, 9]))

