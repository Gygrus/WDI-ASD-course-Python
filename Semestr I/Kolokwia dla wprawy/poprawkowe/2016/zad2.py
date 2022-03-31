"""
 Dana jest N elementowy zbiór liczb naturalnych w postaci tablicy int t[N]. Proszę napisać
funkcję, która zwraca informację czy jest możliwy podział zbioru na trzy zbiory tak aby w każdym z
trzech zbiorów lączna liczba jedynek w liczbach zapisanych w systemie binarnym była jednakowa. Na
przykład dla zbioru |Ż,3,5,7,I1",L3,J-6} możliwy podział to {2,L3,L6} {3,L1i {5,7l czyli w systemie
dwójkowym {10,1101,10000} {11,10LLI |1o1',11'L} - w każdym zbiorze jest 5 jedynek.
"""

def count_ones(t):
    counter = 0
    for x in t:
        while x != 0:
            if x%2 == 1:
                counter += 1

            x //= 2

    return counter



def check(t):



    def rekur(t, z1, z2, z3, i):
        if i == len(t):
            if count_ones(z1) == count_ones(z2) == count_ones(z3):
                print(z1, z2, z3)
                return True

            return False
        z1 = z1[:]
        z2 = z2[:]
        z3 = z3[:]
        return rekur(t, z1+[t[i]], z2, z3, i+1) or rekur(t, z1, z2+[t[i]], z3, i+1) or rekur(t, z1, z2, z3+[t[i]], i+1)

    return rekur(t, list(), list(), list(), 0)


print(check([2,3,5,7,11,13,16]))