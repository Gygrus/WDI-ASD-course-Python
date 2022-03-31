"""
Dana jest N-elementowa tablica t zawierająca liczby naturalne. W tablicy możemy przeskoczyć
z pola o indeksie k o n pól w prawo jeżeli wartość n jest czynnikiem pierwszym liczby t[k]. Napisać funkcję
sprawdzającą czy jest możliwe przejście z pierwszego pola tablicy na ostatnie pole.
"""
from random import randint

N = int(input("> "))

t = [6 for x in range(N)]
print(t)

def check(i):
    tab = [0]
    z = 0
    while 
    while i <= len(t) - 1:

        x = 2
        while t[i] != 1:
            if t[i] % x == 0:
                t[i] /= x
                tab.append(x)
            else:
                x += 1
        for k in tab:



# while i <= len(t) - 1:
#     if i == len(t) - 1:
#         k = True
#         print("Da się!!!")
#     n = 2
#     while n <= t[i]:
#         for k in range(2, n):
#             if n % k == 0:
#                 n += 1
#                 break
#
#         if t[i] % n == 0:
#             i += n
#             break
#         n += 1
#     print("indeks =", i)
#
# if not k:
#     print("Nie da się")

print(check(0))