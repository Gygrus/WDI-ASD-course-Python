"""
Na szachownicy o wymiarach 201 wierszy i 201 kolumn umieszczamy 100 króli szachowych. Proszę
napisać program, który wczytuje z klawiatury położenia 100 króli (wiersz, kolumna), odnajduje dwa
króle jednakowo odległe od środka szachownicy i wypisuje ich pozycję (wiersz, kolumna). W
przypadku gdy żadna para króli nie spełnia warunku program kończy się stosownym komunikatem.
Odległość króla od środka to liczba jego ruchów, które musi wykonać aby dotrzeć do środka
szachownicy.
"""
tab_cords = [0]*100
for x in range(100):
    n_1 = int(input("> "))
    n_2 = int(input("> "))
    n = (n_1, n_2)
    distance = max(abs(100 - n[0]), abs(100 - n[1]))
    for k in tab_cords:
        if k == 0:
            break
        if max((abs(100 - k[0]), abs(100 - k[1]))) == distance:
            print(k, n)

    tab_cords[x] = n

