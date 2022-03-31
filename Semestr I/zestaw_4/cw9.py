"""
Dana jest tablica wypełniona liczbami naturalnymi:
int t[MAX][MAX];
Proszę napisać funkcję, która w poszukuje w tablicy kwadratu o liczbie pól
będącej liczbą nieparzystą większą od 1, którego iloczyn 4 pól narożnych wynosi
k. Do funkcji należy przekazać tablicę i wartość k. Funkcja powinna zwrócić
informacje czy udało się znaleźć kwadrat oraz współrzędne (wiersz, kolumna)
środka kwadratu.
"""

def cw9(t, k):
    for x in range(0, len(t) - 2, 2):
        w_1 = 0             # pierwsza współrzędna "przesuwająca" się po osi x, indeks kolumny lewego górnego oraz lewego dolnego
        w_2 = 2 + x         # druga współrzędna "przesuwająca" się po osi x, indeks kolumny prawego górnego prawego dolnego
        h_1 = 0             # pierwsza współrzędna "przesuwająca" sie po osi y, indeks wiersza lewego górnego oraz prawego górnego
        h_2 = 2 + x         # druga współrzędna "przesuwająca" się po osi y, indeks wiersza lewego dolnego i prawego dolnego
        while w_2 < len(t):
            while h_2 < len(t):
                print(w_1, w_2, h_1, h_2)

                if t[h_1][w_1] * t[h_1][w_2] * t[h_2][w_1] * t[h_2][w_2] == k:
                    return "Udało się znaleźć, środek w punkcie", t[abs(h_1 + h_2)//2][abs(w_1 + w_2)//2]
                h_1 += 1
                h_2 += 1
            w_1 += 1
            w_2 += 1
            h_1 = 0
            h_2 = 2 + x


print(cw9([[1, 6, 34, 64, 3],
           [4, 4, 6, 839, 7],
           [0, 0, 53, 122, 123],
           [1, 4, 1, 64, 1],
           [1, 99, 100, 231, 7]], 21))