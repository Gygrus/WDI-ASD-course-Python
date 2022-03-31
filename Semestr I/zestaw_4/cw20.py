"""
Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
Proszę napisać funkcję która ustawia na szachownicy dwie wieże, tak aby suma liczb na „szachowanych”
przez wieże polach była największa. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić położenie
wież. Uwaga- zakładamy, że wieża szachuje cały wiersz i kolumnę z wyłączeniem pola na którym stoi
"""

def cw20(t):
    result = [0] * 2
    final_result = 0
    for z in range(2):
        biggest = 0
        save = 0
        for x in range(len(t)):
            suma_wiersza = 0
            for i in t[x]:
                suma_wiersza += i

            for y in range(len(t)):
                suma_kolumny = 0
                for i in range(len(t)):
                    suma_kolumny += t[i][y]

                if z == 1:
                    if x == result[0][0]:
                        suma_wiersza = 0
                    if y == result[0][1]:
                        suma_kolumny = 0

                if suma_kolumny + suma_wiersza - 2*(t[x][y]) > biggest and t[x][y] != 0:
                    biggest = suma_kolumny + suma_wiersza - 2*(t[x][y])
                    save = [x, y]

        result[z] = save
        t[result[z][0]][result[z][1]] = 0
        final_result += biggest


    return result, final_result



print(cw20([[4,0,2],[3,0,0],[6,5,3]]))
