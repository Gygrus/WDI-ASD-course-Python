"""
Napisać program wypisujący wszystkie możliwe podziały liczby naturalnej na sumę składników.
Na przykład dla liczby 4 są to: 1+3, 1+1+2, 1+1+1+1, 2+2.
"""

def podzial(n, k=1, l=''):
    if n == 0 and l.count('+') > 1: print(l[:-1])
    else:
        for i in range(k, n+1):
            podzial(n-i, i, l+str(i)+'+')

podzial(160)