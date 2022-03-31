"""
Dana jest liczba naturalna N niezawierająca cyfry 0, którą rozbijamy na dwie liczby naturalne
A i B, przenosząc kolejne cyfry z liczby N do liczby A albo B. Na przykład liczbę 21523
możemy rozbić na wiele sposobów, np. (215,23),(2,1523),(223,15),(152,23),(22,153),(1,2523)...
Uwaga: względna kolejność cyfr w liczbie N oraz liczbach A i B musi być zachowana. Proszę
napisać funkcję generującą i wypisującą wszystkie rozbicia, w których powstałe liczby A i B
są względnie pierwsze. Do funkcji należy przekazać wartość N, funkcja powinna zwrócić liczbę
znalezionych par.
"""



def f(n):

    binar = 2**len(str(n))
    count = 0
    for x in range(binar//2):
        check = ''
        while x != 0:
            check += str(x%2)
            x //= 2

        while len(check) != len(str(n)):
            check += '0'
        print(check)

        A = 0
        B = 0
        i = 0
        for k in str(n):
            if check[i] == '1':
                A *= 10
                A += int(str(n)[i])

            else:
                B *= 10
                B += int(str(n)[i])

            i += 1

        z = True
        p = 2
        while p <= A and p <= B:
            if A % p == 0 and B % p == 0:
                z = False
                break
            p += 1

        if z and A != 0 and B != 0:
            # print(A, B)
            count += 1

    return count



print(f(9836))