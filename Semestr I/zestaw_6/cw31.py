"""
Proszę napisać funkcję, która jako parametr otrzymuje liczbę naturalną i zwraca sumę
iloczynów elementów wszystkich niepustych podzbiorów zbioru podzielników pierwszych tej liczby. Można założyć,
że liczba podzielników pierwszych nie przekracza 20, zatem w pierwszym etapie funkcja powinna wpisać podzielniki
do tablicy pomocniczej. Przykład: 60 → [2, 3, 5] → 2 + 3 + 5 + 2 ∗ 3 + 2 ∗ 5 + 3 ∗ 5 + 2 ∗ 3 ∗ 5 = 71
"""


def rekur(n):
    i = 2
    tab = [0]*20
    counter = 0
    while n != 1:
        if n % i == 0:
            tab[counter] = i
            counter += 1
            while n % i == 0:
                n //= i
        i += 1
    new_tab = [0]*(20-tab.count(0))
    i = 0
    for x in tab:
        if x == 0:
            break
        else:
            new_tab[i] = x
            i += 1

    print(new_tab)

    licznik = 0
    def find_sum(new_tab, brand_new_tab, i):
        print(brand_new_tab)
        if i == len(new_tab):
            if len(brand_new_tab) > 0:
                k = 1
                for x in brand_new_tab:
                    k *= x
                nonlocal licznik
                licznik += k

        else:
            find_sum(new_tab, brand_new_tab, i+1)
            brand_new_tab = list(brand_new_tab)
            brand_new_tab.append(new_tab[i])
            brand_new_tab = tuple(brand_new_tab)
            find_sum(new_tab, brand_new_tab, i+1)

    find_sum(new_tab, tuple(), 0)
    return licznik


print(rekur(631375430))
