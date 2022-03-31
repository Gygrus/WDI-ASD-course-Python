"""
Dwie liczby naturalne są „przyjaciółkami jeżeli zbiory cyfr z których zbudowane
są liczby są identyczne. Na przykład: 123 i 321, 211 i 122, 35 3553. Dana jest
tablica int t[MAX][MAX] wypełniona liczbami naturalnymi. Proszę napisać
funkcję, która dla tablicy t zwraca ile elementów tablicy sąsiaduje wyłącznie z
przyjaciółkami
"""

def cw11(t):
    for x in range(len(t)):
        for i in range(len(t)):
            new = set([0]*len(str(t[x][i])))
            a = 0
            for x in str(t[x][i]):
                print(x)
                new[a].append(x)
                a += 1
            print(new)
            t[x][i] = set(new)
    count = 0
    print(t)
    for x in range(len(t)):
        for i in range(len(t)):
            if x > 0 and x < len(t) - 1 and i > 0 and i < len(t) - 1:
                if t[x][i] == t[x-1][i-1] == t[x-1][i] == t[x-1][i+1] == t[x][i-1] == t[x][i+1] == t[x+1][i-1] == t[x+1][i] == t[x+1][i+1]:
                    count += 1
            elif x == 0 and i > 0 and i < len(t) - 1:
                if t[x][i] == t[x][i-1] == t[x][i+1] == t[x+1][i-1] == t[x+1][i] == t[x+1][i+1]:
                    count += 1



print(cw11([[1, 6, 34, 0, 3],
           [0, 4, 6, 839, 7],
           [0, 7, 53, 122, 0],
           [1, 4, 1, 0, 1],
           [1, 0, 0, 231, 7]]))