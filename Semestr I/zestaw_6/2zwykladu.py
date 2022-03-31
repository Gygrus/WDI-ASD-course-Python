"""
Dana jest tablica T[N] zawierająca nieuporządkowane
liczby naturalne. Proszę zmodyfikować funkcję qs, tak aby
szybko wyznaczyć sumę k najmniejszych wartości z tablicy.
Przykładowe dane to N=1000000 i k=50.
"""
from random import randint

def qs(T, k):
    result = 0
    def qsrt(T, l, p, k):
        nonlocal result
        #print(l, k)
        if l >= k or p <= k:
            result = sum(T[:k])
        else:
            i = l
            j = p
            x = T[(i+j)//2]
            while i <= j:
                while T[i] < x:
                    i += 1
                while T[j] > x:
                    j -= 1
                if i <= j:
                    T[j], T[i] = T[i], T[j]
                    i += 1
                    j -= 1

            if l < j:
                qsrt(T, l, j, k)
            if p > i:
                qsrt(T, i, p, k)

    qsrt(T, 0, len(T)-1, k)
    return result

T = [randint(1, 156430) for _ in range(1000000)]
#print(T)
print(qs(T, 65))
#print(T)
#print(result)