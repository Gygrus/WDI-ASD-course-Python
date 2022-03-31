"""
Dana jest tablica booli int t[N][N] reprezentująca szachownicę. Pole szachownicy ma
wartość true, jeżeli stoi na nim figura, a false, jeśli jest ono puste. Proszę napisać
funkcję która sprawdza czy istnieje droga skoczka przemieszczającego się z wiersza
0 do wiersza N-1. Skoczek może poruszać się tylko po polach pustych. Skoczek w
każdym ruchu powinien przybliżać się do N-1 wiersza. Funkcja ma zwrócić
najmniejszą możliwą liczbę ruchów. Skoczek może zacząć poruszać się z dowolnego
pustego pola z wiersza 0. N z zakresu 4...20.
"""

def check_if_exists(T):
    validation = False
    def rekur(T, x, y, tab):
        print(x, y)
        if x >= len(T) or y >= len(T) or y < 0:
            return
        if not T[x][y]:
            tab = tab[:]
            tab.append((x, y))
            nonlocal validation
            if x == len(T) - 1:
                validation = True
                print(tab)
                return

            if not validation:
                rekur(T, x+1, y-2, tab)
                rekur(T, x+1, y+2, tab)
                rekur(T, x+2, y+1, tab)
                rekur(T, x+2, y-1, tab)

    for x in range(len(T)):
        if validation:
            break
        if x > 3:
            if x > 20:
                break
            rekur(T, 0, x, [])

    return validation

t = [[0, 0, 0, 0, 1, 0, 1, 0, 0],
     [1, 1, 0, 1, 0, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 1, 1, 0, 1],
     [1, 1, 0, 1, 0, 0, 1, 1, 0],
     [0, 1, 1, 0, 1, 0, 0, 1, 0],
     [1, 1, 0, 1, 0, 1, 1, 0, 1],
     [1, 1, 1, 1, 1, 1, 1, 0, 0],
     [1, 1, 1, 1, 0, 0, 1, 0, 1],
     [1, 1, 0, 1, 0, 1, 1, 0, 0]
    ]


print(check_if_exists(t))