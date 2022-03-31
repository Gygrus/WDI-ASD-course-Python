"""
W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy króla
nałożono dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra liczby na
polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do obranego celu
(np. narożnika) król nie może wykonać ruchu, który powoduje oddalenie go od celu. Dana jest globalna tablica
T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę. Lewy górny narożnik ma współrzędne
w=0 i k=0. Proszę napisać funkcję sprawdzającą czy król może dostać się z pola w,k do prawego dolnego
narożnika.
"""
from random import randint

def func(T, w_cur, k_cur, w_last, k_last):
    if w_cur == k_cur and w_cur == len(T) - 1:
        if (T[w_cur][k_cur] // 10**(len(str(T[w_cur][k_cur])) - 1)) > (T[w_last][k_last] % 10):
            return True
    elif w_cur == len(T) - 1:
        if (T[w_cur][k_cur] // 10**(len(str(T[w_cur][k_cur])) - 1)) > (T[w_last][k_last] % 10):
             return func(T, w_cur, k_cur + 1, w_cur, k_cur)
    elif k_cur == len(T) - 1:
        if (T[w_cur][k_cur] // 10**(len(str(T[w_cur][k_cur])) - 1)) > (T[w_last][k_last] % 10):
            return func(T, w_cur + 1, k_cur, w_cur, k_cur)
    elif (T[w_cur][k_cur] // 10**(len(str(T[w_cur][k_cur])) - 1)) > (T[w_last][k_last] % 10):

        return func(T, w_cur, k_cur + 1, w_cur, k_cur) or func(T, w_cur + 1, k_cur + 1, w_cur, k_cur) or func(T, w_cur + 1, k_cur, w_cur, k_cur)



#T = [[randint(1, 9) for _ in range(5)] for _ in range(5)]
T = [[1,2,3],[1,2,3],[1,2,3]]

for x in T:
    print(x)

def rekur(T):
    return func(T, 0, 1, 0, 0) or func(T, 1, 1, 0, 0) or func(T, 1, 0, 0, 0)


print(rekur(T))



