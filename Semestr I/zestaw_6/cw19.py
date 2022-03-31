"""
W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy króla
nałożono dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra liczby na
polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do obranego celu
(np. narożnika) król nie może wykonać ruchu, który powoduje oddalenie go od celu. Dana jest globalna tablica
T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę. Lewy górny narożnik ma współrzędne
w=0 i k=0. Proszę napisać funkcję sprawdzającą czy król może dostać się z pola w,k do prawego dolnego
narożnika.
Zadanie 19. Zadanie jak powyżej. Funkcja sprawdzająca czy król
może dostać się z pola w,k do któregokolwiek z narożników
"""
from random import randint


def can_it_go(t, p1, p2):
    last_of_first = t[p1[0]][p1[1]] % 10
    get_len = 0
    x = t[p2[0]][p2[1]]
    while x != 0:
        get_len+=1
        x //= 10

    first_of_second = t[p2[0]][p2[1]] // 10**(get_len-1)

    if last_of_first < first_of_second:
        return True

    return False

def check_if_possible(t, w, x):

    result = False
    def rekur(t, w, k, dest, tab):
        print(w, k)
        nonlocal result, result0, result1, result2, result3
        tab = tab[:]
        tab.append((w, k))
        if (w, k) == result0 or (w, k) == result1 or (w, k) == result2 or (w, k) == result3:
            result = True
            print(tab)
            return

        if not result:
            if dest == 0:
                if w > 0 and k > 0:
                    if can_it_go(t, (w, k), (w-1, k-1)):
                        rekur(t, w-1, k-1, dest, tab)
                if w > 0:
                    if can_it_go(t, (w, k), (w-1, k)):
                        rekur(t, w-1, k, dest, tab)
                if k > 0:
                    if can_it_go(t, (w, k), (w, k-1)):
                        rekur(t, w, k-1, dest, tab)

            elif dest == 1:
                if w > 0 and k < len(t)-1:
                    if can_it_go(t, (w, k), (w-1, k+1)):
                        rekur(t, w-1, k+1, dest, tab)
                if w > 0:
                    if can_it_go(t, (w, k), (w-1, k)):
                        rekur(t, w-1, k, dest, tab)
                if k < len(t)-1:
                    if can_it_go(t, (w, k), (w, k+1)):
                        rekur(t, w, k+1, dest, tab)

            elif dest == 2:
                if w < len(t) - 1 and k > 0:
                    if can_it_go(t, (w, k), (w-1, k-1)):
                        rekur(t, w-1, k-1, dest, tab)
                if w < len(t) - 1:
                    if can_it_go(t, (w, k), (w-1, k)):
                        rekur(t, w-1, k, dest, tab)
                if k > 0:
                    if can_it_go(t, (w, k), (w, k-1)):
                        rekur(t, w, k-1, dest, tab)

            elif dest == 3:
                if w < len(t)-1 and k < len(t)-1:
                    if can_it_go(t, (w, k), (w+1, k+1)):
                        rekur(t, w+1, k+1, dest, tab)
                if w < len(t)-1:
                    if can_it_go(t, (w, k), (w+1, k)):
                        rekur(t, w+1, k, dest, tab)
                if k < len(t)-1:
                    if can_it_go(t, (w, k), (w, k+1)):
                        rekur(t, w, k+1, dest, tab)
    result0 = (0, 0)
    result1 = (0, len(t)-1)
    result2 = (len(t)-1, 0)
    result3 = (len(t)-1, len(t)-1)
    for z in range(4):
        if not result:
            rekur(t, w, x, z, list())

    return result


t = [[randint(1, 10) for _ in range(8)] for _ in range(8)]
for x in t:
    print(x)


print(check_if_possible(t, 3, 3))