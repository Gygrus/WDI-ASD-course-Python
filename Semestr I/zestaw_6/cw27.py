"""
Kwadrat jest opisywany czwórką liczb całkowitych (x1, x2, y1, y2), gdzie x1, x2, y1, y2 oznaczają proste ograniczające kwadrat x1 < x2, y1 < y2. Dana jest tablica T zawierająca opisy N kwadratów. Proszę
napisać funkcję, która zwraca wartość logiczną True, jeśli danej tablicy można znaleźć 13 nienachodzących
na siebie kwadratów, których suma pól jest równa 2012 i False w przeciwnym przypadku.
"""
def check_if_correct(tab):
    suma = 0
    for p in tab:
        suma += (p[1] - p[0])**2
    print(tab, suma)
    if suma != 74:
        return False
    else:
        for x in range(len(tab)):
            for y in range(x+1, len(tab)):
                if tab[x][0] < tab[y][0] and tab[x][1] > tab[y][1]:
                    if tab[x][2] > tab[y][2] or tab[x][3] < tab[y][3]:
                        return False

                elif tab[x][0] > tab[y][0] and tab[x][1] < tab[y][1]:
                    if tab[x][2] < tab[y][2] or tab[x][3] > tab[y][3]:
                        return False

                else:
                    return False

        return True

def costam(T):
    z = False
    def rekur(T, set_of_squares, i):
        print(set_of_squares)
        if i == len(T):
            if len(set_of_squares) == 4 and check_if_correct(set_of_squares):
                print('hurraaaa')
                nonlocal z
                z = True
        else:
            rekur(T, set_of_squares, i+1)
            set_of_squares = list(set_of_squares)
            set_of_squares.append(T[i])
            set_of_squares = tuple(set_of_squares)
            rekur(T, set_of_squares, i+1)

    rekur(T, tuple(), 0)

    return z

#T = [[randint(-50, 50) for _ in range(4)] for _ in range(13)]
T = [[1, 3, 0, 2], [0, 4, -1, 3], [4, 9, 0, 5], [-12, -6, 99, 105], [17, 20, 4, 7]]
print(check_if_correct(T))
print(costam(T))