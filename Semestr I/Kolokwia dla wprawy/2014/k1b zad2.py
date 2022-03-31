"""
 Dane są dwie tablice mogące pomieścić taką samą liczbę elementów:
 int t1[10][N];
 int t2[M]; // M = 10*N
W każdym wierszu tablicy t1 znajdują się uporządkowane rosnąco (w obrębie wiersza) liczby
naturalne.
Proszę napisać fragment programu przepisujący wszystkie singletony (liczby występujące dokładnie
raz) z tablicy t1 do t2, tak aby liczby w tablicy t2 były uporządkowane rosnąco. Pozostałe elementy
tablicy t2 powinny zawierać zera.
"""
from random import randint


N = int(input(">"))
t2 = [0]*(10*N)
t1 = [[randint(1, 20) for _ in range(N)] for _ in range(10)]
for x in t1:
    print(x)

# new = [0]*(10*N)
# k = 0
# for x in t1:
#     for y in x:
#         new[k] = y
#         k += 1
# print(new)
# for x in range(len(new) - 1):
#     z = True
#     if new[x] not in t2:
#         for y in range(len(new)):
#             if y != x:
#                 if new[x] == new[y]:
#                     z = False
#                     break
#
#         temp = new[x]
#         if z:
#             print(new[x], x, y)
#             for k in range(len(t2) - 1, -1, -1):
#                 if temp == 0:
#                     break
#                 if t2[k] < temp:
#                     a = t2[k]
#                     t2[k] = temp
#                     temp = a

for x in range(10*N):
    z = True
    for y in range(10*N):
        if x != y:
            if t1[x%10][x//10] == t1[y%10][y//10]:
                z = False
                break

    temp = t1[x%10][x//10]
    if z:
        for k in range(len(t2) - 1, -1, -1):
            if temp == 0:
                break
            if t2[k] < temp:
                a = t2[k]
                t2[k] = temp
                temp = a

print(t2)




