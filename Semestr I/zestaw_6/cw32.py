"""
 Dana jest tablica T[N] zawierająca liczby naturalne. Proszę napisać funkcję, która odpowiada
na pytanie, czy spośród (niekoniecznie wszystkich) elementów tablicy można utworzyć dwa podzbiory o
jednakowej sumie elementów, tak aby suma mocy obu podzbiorów wynosiła k. Do funkcji należy przekazać
wyłącznie tablicę T oraz liczbę naturalną k, funkcja powinna zwrócić wartość typu bool.
"""

def rekur(T, k):

    def check_if_exists(T, podzb1, podzb2, i, k):
        #print(podzb1, podzb2)
        if i == len(T):
            if len(podzb1) > 0 and len(podzb2) > 0:
                if sum(podzb1) + sum(podzb2) == k:
                    return True
                else:
                    return False
        else:
            new_tuple_1 = list(podzb1)
            new_tuple_1.append(T[i])
            new_tuple_1 = tuple(new_tuple_1)
            new_tuple_2 = list(podzb2)
            new_tuple_2.append(T[i])
            new_tuple_2 = tuple(new_tuple_2)
            return check_if_exists(T, podzb1, podzb2, i+1, k) or check_if_exists(T, new_tuple_1, podzb2, i+1, k) or check_if_exists(T, podzb1, new_tuple_2, i+1, k)

    return check_if_exists(T, tuple(), tuple(), 0, k)

print(rekur([2, 43, 25, 32, 43, 32, 32, 52, 3, 1, 2], 41))
