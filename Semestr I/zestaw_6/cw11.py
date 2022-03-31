"""
Dana jest tablica T[N]. Proszę napisać program zliczający liczbę “enek” o określonym iloczynie.
"""
from random import randint

def rekur(T, result):
    licznik = 0


    def count_n(T, i, set_of_n, mult, result, mass_list):
        if i == len(T):
            if mult == result and set_of_n not in mass_list:
                print(set_of_n, "jest to", len(set_of_n), '-ka')
                nonlocal licznik
                licznik += 1
                mass_list.append((set_of_n))
        else:
            count_n(T, i+1, set_of_n, mult, result, mass_list)
            set_of_n = list(set_of_n)
            set_of_n.append(T[i])
            set_of_n = tuple(set_of_n)
            count_n(T, i+1, set_of_n, mult*T[i], result, mass_list)

    set_of_n = tuple()
    count_n(T, 0, set_of_n, 1, result, list())
    return licznik


T = [randint(1, 10) for _ in range(10)]
for x in T:
    print(x)

print(rekur(T, 8))