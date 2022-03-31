"""
Dana jest N-elementowa tablica t zawierająca liczby naturalne mniejsze od 1000.
Proszę napisać funkcję, która zwraca długość najdłuższego, spójnego fragmentu
tablicy, dla którego w iloczynie jego elementów każdy czynniki pierwszy występuje
co najwyżej raz. Na przykład dla tablicy t=[2,23,33,35,7,4,6,7,5,11,13,22]
wynikiem jest wartość 5.
"""
from random import randint

def cw20(t):
    k = len(t)
    biggest = 0
    while k > 0:
        i = 0
        while i != k:
            new = t[i:k]
            mult = 1
            for x in new:
                mult *= x
            n = 2
            ctrl_tab = []
            z = True
            while mult != 1:
                if mult % n == 0:
                    mult //= n
                    ctrl_tab.append(n)
                    if ctrl_tab.count(n) > 1:
                        z = False
                        break
                else:
                    n += 1
            if z and len(new) > biggest:
                biggest = len(new)
                result = new


            i += 1
        k -= 1
    return biggest, result

t = [randint(1, 1000) for x in range(1000)]
print(cw20(t))