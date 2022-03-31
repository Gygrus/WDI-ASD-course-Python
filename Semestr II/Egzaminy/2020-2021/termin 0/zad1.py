"""Rozważmy słowa x[0]x[1] · · · x[n − 1] oraz y[0]y[1] · · · y[n − 1] składające się z małych liter alfabetu łacińskiego. Takie dwa słowa są t-anagramem (dla t ∈ {0, . . . , n − 1}), jeśli każdej literze
pierwszego słowa można przypisać taką samą literę drugiego, znajdującą się na pozycji różniącej
się o najwyżej t, tak że każda litera drugiego słowa jest przypisana dokładnie jednej literze słowa
pierwszego.
Proszę zaimplementować funkcję:
def tanagram(x, y, t):
...
która sprawdza czy słowa x i y są t-anagramami i zwraca True jeśli tak a False w przeciwnym razie. Funkcja powinna być możliwie jak najszybsza. Proszę oszacować złożoność czasową
i pamięciową użytego algorytmu.
Przykład. Słowa ”kotomysz” oraz ”tokmysoz” są 3-anagramami, ale nie są 2-anagramami:
0 1 2 3 4 5 6 7  0 1 2 3 4 5 6 7 - nr litery w słowie
2 1 0 6 3 4 5 7  2 1 0 4 5 6 3 7 - nr litery przypisanej w drugim słowie
k o t o m y s z  t o k m y s o z
"""

"""
O(t*n)
"""
def tanagram(x, y, t):
    n = len(x)
    tab = [0]*n
    for i in range(n):
        check = False
        for j in range(i-t, i+t+1):
            if j >= 0 and j <= n-1:
                if x[i] == y[j] and tab[j] < 1:
                    tab[j] += 1
                    check = True
                    break

        if not check:
            return False

    return check

# x = "kotomysz"
# y = "tokmysoz"
# print(tanagram(x, y, 3))

# 26 = k
def tanagram1(x, y, t):
    def countsort(A, k):
        C = [0] * k
        B = [0] * len(A)
        for i in range(len(A)):
            C[ord(A[i][0])-97] += 1

        for i in range(1, k):
            C[i] += C[i - 1]

        for i in range(len(A) - 1, -1, -1):
            C[ord(A[i][0])-97] -= 1
            B[C[ord(A[i][0])-97]] = A[i]

        for i in range(len(A)):
            A[i] = B[i]

    n = len(x)
    x_tab = [[None, 0] for _ in range(n)]
    y_tab = [[None, 0] for _ in range(n)]
    for i in range(n):
        x_tab[i][0] = x[i]
        x_tab[i][1] = y_tab[i][1] = i
        y_tab[i][0] = y[i]

    countsort(x_tab, 26)
    countsort(y_tab, 26)
    print(x_tab)
    print(y_tab)

    for i in range(n):
        if x_tab[i][0] != y_tab[i][0] or abs(x_tab[i][1] - y_tab[i][1]) > t:
            return False

    return True

x = "kotomysz"
y = "tokmysoz"
print(tanagram1(x, y, 3))