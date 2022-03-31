"""
Mamy dany ciąg napisów S = (s1, ..., sn) oraz pewien napis t. Wiadomo, że t można zapisać jako
złączenie pewnej ilości napisów z S (z powtórzeniami). Na przykład dla S = (s1, s2, s3, s4, s5)
gdzie s1 = ab, s2 = abab, s3 = ba oraz s4 = bab, s5 = b, napis t = ababbab można zapisać, między
innymi, jako s2s4 lub jako s1s1s3s5. Pierwsza reprezentacja ma ”szerokość” 3 (przez szerokość
rozumiemy długość najkrótszego si użytego w reprezentacji) a druga 1. Proszę opisać algorytm,
który mając na wejściu S oraz t znajdzie maksymalną szerokość reprezentacji t.
Proszę oszacować czas działania algorytmu.
"""

"""
f(i) = maksymalna szerokość reprezentacji do indeksu i-tego napisu t
f(i) = max( min(f(i-len(s)), len(s))) if len(s) <= i and t[i-len(s):i] == s po wszystkich s ze zbioru S if 
f(0) = 0 if nie ma len(s) == 1 and t[0] == s
złożoność obliczeniowa: O(n^2)
"""
from math import inf

def finding_width(S, t):
    n = len(t)
    F = [0]*(n+1)
    F[0] = inf
    for s in S:
        if len(s) == 1 and s == t[0]:
            F[1] = 1
            break

    for i in range(2, n+1):
        for s in S:
            if len(s) <= i:
                if s == t[i-len(s):i]:
                    print(s, i)
                    z = min(F[i-len(s)], len(s))
                    if z > F[i]:
                        F[i] = z

    print(F)
    return F[n]

s1 = "ab"
s2 = "abab"
s3 = "bab"
s4 = "baba"
s5 = "b"
t = "ababbaba"

S = [s1,s2,s3,s4,s5]
print(finding_width(S, t))