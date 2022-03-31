"""
Dany jest zbiór przedziałów otwartych A = {(a1, b1), ...,(an, bn)}. Proszę zaproponować algorytm
(bez implementacji), który znajduje taki zbiór X, X ⊆ {1, ..., n} że (a) |X| = k (gdzie k ∈ N to
dany parametr wejściowy), (b) dla każdych i, j ∈ X, przedziały (ai, bi) oraz (aj, bj ) nie nachodzą
na siebie, oraz (c) wartość maxj∈Xbj − mini∈Xai
jest minimalna. Jeśli podzbioru spełniającego
warunki (a) i (b) nie ma, to algorytm powinien to stwierdzić. Algorytm powinien być możliwie
jak najszybszy (ale przede wszystkim poprawny).
"""
"""
Rozwiązanie dynamiczne
najpierw sortuję przedziały po pierwszej współrzędnej - O(nlogn)
f(i, j) = 
1. maksymalna liczność zbioru X (z ograniczeniem górnym k), 
który można uzyskać gdzie początkowym przedziałem jest przedział i, a rozważamy przedziały do j włącznie,
2. druga współrzędna ostatniego przedziału z naszego zbioru X 
3. wartość max_j - min_i
F[i][j] = {
1. F[i][j-1][0] = 1:
    [F[i][j-1][0]+1, A[j][1], A[j][1]-A[i][0]] if A[j][0] > F[i][j-1][1]
    else:
        F[i][j-1] 
2. F[i][j-1][0] < k and F[i][j-1][0] > 1:
    [F[i][j-1][0]+1, A[j][1], A[j][1]-A[i][0]] if A[j][0] > F[i][j-1][1]
    [F[i][j-1][0], A[j][1], A[j][1]-A[i][0]] if A[j][1] < F[i][j-1][1]
    else:
        F[i][j-1]
3. F[i][j-1][0] == k:
    [F[i][j-1][0], A[j][1], A[j][1]-A[i][0]] if A[j][1] < F[i][j-1][1]
    else:
        F[i][j-1]
        
F[i][i] = [1, A[i][1], A[i][1]-A[i][0]] dla i należących od 1 do n
odczytanie wyniku:
od i = 1 do n min(F[i][n][2]) if F[i][n][0]==k
złożoność pamięciowa i obliczeniowa: O(n^2)
"""