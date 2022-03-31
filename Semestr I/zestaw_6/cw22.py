"""
Dana jest tablica T[N] zawierająca liczby naturalne. Po tablicy możemy przemieszczać się
według następującej zasady: z pola o indeksie i możemy przeskoczyć na pole o indeksie i+k jeżeli k jest
czynnikiem pierwszym liczby t[i] mniejszym od t[i]. Proszę napisać funkcję, która zwraca informację czy jest
możliwe przejście z pola o indeksie 0 na pole o indeksie N-1. Funkcja powinna zwrócić liczbę wykonanych
skoków lub wartość -1 jeżeli powyższe przejście nie jest możliwe.
"""
from random import randint

def get_all_primes(n):
    copy = n
    if n == 1 or n == 2 or n == 3:
        return 0
    tab = []
    k = 2
    while n != 1:
        if n % k == 0:
            if k == copy:
                return 0
            tab.append(k)
            while n % k == 0:
                n //= k
        k += 1

    return tab

def rekur(T):
    min_count = 10**100

    def jumps(T, i, count):
        #print(i, count)
        if i >= len(T):
            return False
        if i == len(T) - 1:
            #print(count)
            nonlocal min_count
            if count <= min_count:
                min_count = count
        else:
            if not get_all_primes(T[i]):
                return False

            else:
                k = get_all_primes(T[i])
                #print("k", k, 'i', i)
                for x in k:
                    jumps(T, i+x, count + 1)


    jumps(T, 0, 0)
    if min_count > len(T):
        return -1
    else:
        return min_count


T = [randint(10, 10) for _ in range(11)]
print(T)
print(rekur(T))