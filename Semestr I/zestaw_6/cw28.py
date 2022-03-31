"""
Dany jest zbiór N liczb naturalnych umieszczony w tablicy T[N]. Proszę napisać funkcję,
która zwraca informację, czy jest możliwy podział zbioru N liczb na trzy podzbiory, tak aby w każdym
podzbiorze, łączna liczba jedynek użyta do zapisu elementów tego podzbioru w systemie dwójkowym była
jednakowa. Na przykład: [2, 3, 5, 7, 15] → true, bo podzbiory {2,7} {3,5} {15} wymagają użycia 4 jedynek,
[5, 7, 15] → f alse, podział nie istnieje.
"""

def binary_check(num):
    count = 0
    while num != 0:
        if num % 2 == 1:
            count += 1
        num //= 2
    return count



def rekur(T, s1, s2, s3, i):
    print(s1, s2, s3)
    if i == len(T):
        if s1 == s2 and s1 == s3:
            return True
    else:
        x = binary_check(T[i])
        return rekur(T, s1 + x, s2, s3, i+1) or rekur(T, s1, s2 + x, s3, i+1) or rekur(T, s1, s2, s3 + x, i+1)



print(rekur([5, 7, 15], 0, 0, 0, 0))