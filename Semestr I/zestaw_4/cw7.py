"""
Dane są dwie tablice mogące pomieścić taką samą liczbę elementów:
int t1[MAX][MAX];
int t2[MAX2]; // MAX2 = MAX*MAX
W każdym wierszu tablicy t1 znajdują się uporządkowane niemalejąco (w obrębie
wiersza) liczby naturalne. Proszę napisać funkcję przepisującą wszystkie liczby
z tablicy t1 do t2, tak aby liczby w tablicy t2 były uporządkowane niemalejąco.
"""

def cw7(t1, t2):
    for x in t1:
        for i in x:
            a = len(t2) - 1
            while i != 0:
                if i > t2[a]:
                    chwilowa = t2[a]
                    t2[a] = i
                    i = chwilowa
                a -= 1

    return t2


t1 = [[3, 6, 34, 64, 64],
      [4, 4, 99, 234, 254],
      [0, 0, 0, 122, 123],
      [1, 4, 23, 64, 98],
      [99, 99, 100, 231, 5125]]

print(cw7(t1, [0]*len(t1)**2))