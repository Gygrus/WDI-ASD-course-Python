"""
[2pkt.] Zadanie 3. Dany jest zbiór klocków K = {K1, . . . , Kn}. Każdy klocek Ki opisany
jest jako jednostronnie domknięty przedział (ai, bi], gdzie ai, bi ∈ N, i ma wysokość 1 (należy
założyć, że żadne dwa klocki nie zaczynają się w tym samym punkcie, czyli wartości ai są
parami różne). Klocki są zrzucane na oś liczbową w pewnej kolejności. Gdy tylko spadający
klocek dotyka innego klocka (powierzchnią poziomą), to jest do niego trwale doczepiany i
przestaje spadać. Kolejność spadania klocków jest poprawna jeśli każdy klocek albo w całości
ląduje na osi liczbowej, albo w całości ląduje na innych klockach. Rozważmy przykładowy
zbiór klocków K = {K1, K2, K3, K4}, gdzie:
K1 = (2, 4], K2 = (5, 7], K3 = (3, 6], K4 = (4, 5].
Kolejność K1, K4, K2, K3 jest poprawna (choć są też inne poprawne kolejności) podczas gdy
kolejność K1, K2, K3, K4 poprawna nie jest (K3 nie leży w całości na innych klockach):

Proszę podać algorytm (bez implementacji), który sprawdza czy dla danego zbioru klocków
istnieje poprawna kolejność spadania. Proszę uzasadnić poprawność algorytmu oraz oszacować
jego złożoność. Proszę także odpowiedzieć na następujące pytanie:
Czy jeśli początki klocków nie muszą być parami różne to algorytm dalej działa poprawnie?
Jeśli tak, proszę to uzasadnić. Jeśli nie, to proszę podać kontrprzykład.
"""

"""
Sortuję klocki po ich pierwszej współrzędnej, następnie ustawiam pierwszy klocek na ziemi (musi być tam połączony, 
bo nie ma innego klocka, który mógłby w całości "objąć" klocek o najwcześniejszym początku). Zapisuję koniec położonego
klocka i szukam kolejnego klocka o początku większym niż zapisany koniec i ustawiam go na rozważanym poziomie. 
Musi on być położony na tym poziomie, bo jeśli nie byłby na nim położony, to "wystawałby" lewym końcem z klocka
o późniejszym początku, na którym byłby położony. Za każdym razem jeśli powstaje przerwa w warstwie, zapisuję ją.
Po wyłożeniu danej warstwy rozważamy kolejne warstwy przeszukując pozostałe klocki, jeśli początek, albo koniec któregoś z 
końców zawiera się w przerwie w poprzednim poziomie, to oznacza, że nie istnieje poprawna kolejność spadania dla danych klocków. 
"""

def quicksort1(Tab, p, r):
    def quicksort(Tab, p, r):
        while p < r:
            q = partition(Tab, p, r)
            quicksort(Tab, p, q-1)
            p = q + 1

    def partition(Tab, p, r):
        x = Tab[r][0]
        i = p-1
        for j in range(p, r):
            if Tab[j][0] < x:
                i += 1
                Tab[i], Tab[j] = Tab[j], Tab[i]
        Tab[i+1], Tab[r] = Tab[r], Tab[i+1]
        return i+1

    quicksort(Tab, p, r)

def put_blocks(K):
    n = len(K)
    quicksort1(K, 0, n-1)
    print(K)
    checklist = [False]*n
    check_number = 0
    left_end = K[0][0]
    right_end = 99999
    right_end_temp = left_end
    tab_of_space = []
    while check_number != n:
        for x in range(n):
            if not checklist[x]:
                left_end = K[x][0]
                break
        right_end_temp = left_end
        for x in range(n):
            if K[x][0] >= right_end_temp and not checklist[x]:
                checklist[x] = True
                check_number += 1
                if (K[x][1] > right_end):
                    return False
                for i in tab_of_space:
                    if (K[x][0] > i[0] and K[x][0] < i[1]) or (K[x][1] > i[0] and K[x][1] < i[1]):
                        return False
                if K[x][0] - right_end_temp > 0:
                    tab_of_space.append((right_end_temp, K[x][0]))
                right_end_temp = K[x][1]
        right_end = right_end_temp

    return True

K1 = [2, 3]
K2 = [5, 7]
K3 = [3, 6]
K4 = [4, 5]


K = [K1, K2, K3, K4]
print(put_blocks(K))