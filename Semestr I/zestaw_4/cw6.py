"""
Dane są dwie tablice mogące pomieścić taką samą liczbę elementów:
int t1[MAX][MAX];
int t2[MAX2]; // MAX2 = MAX*MAX
W każdym wierszu tablicy t1 znajdują się uporządkowane rosnąco (w obrębie
wiersza) liczby naturalne. Proszę napisać funkcję przepisującą wszystkie
singletony (liczby występujące dokładnie raz) z tablicy t1 do t2, tak aby
liczby w tablicy t2 były uporządkowane rosnąco. Pozostałe elementy tablicy t2
powinny zawierać zera.
"""


def cw6(t1, t2):
    new = [0]*len(t1)**2
    a = 0
    for x in t1:
        for i in x:
            new[a] = i
            a += 1
    print(new)
    for x in new:
        if new.count(x) == 1:
            obecna = x
            a = len(t2) - 1
            while obecna != 0:
                if obecna > t2[a]:
                    chwilowa = t2[a]
                    t2[a] = obecna
                    obecna = chwilowa
                a -= 1

    return t2


t1 = [[3, 6, 34, 64],
      [53, 4, 99, 234],
      [53, 62, 100, 122],
      [1, 4, 234, 64]]

print(t1[1].count(4))
print(cw6(t1, [0]*(len(t1)**2)))