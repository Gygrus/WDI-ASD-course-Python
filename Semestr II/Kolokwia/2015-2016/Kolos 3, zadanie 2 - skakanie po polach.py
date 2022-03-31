"""
struct field {
int value;
int long j;
int short j;
};
Z każdego pola można skakać tylko o ilość pól zapisaną w long j lub short j. Napisać program
który zwróci maksymalną wartość jaką możemy osiągnąć poprzez przejście z pola 0 do n-1.
Można założyć że z każdego pola da się dojść do pola n-1.
"""

"""
funkcja f(i) = maksymalna wartość jaką możemy osiągnąć z przejścia z pola i do n-1
f(i) = max(f(i + long_j) + (i+long_j).value, f(i + short_i) + (i+short_j).value), if i+short_j < n, i+long_j < n
f(n-1) = 0
wynik odczytujemy z f(0)
Złożoność: O(n), jeśli mamy n pól
"""

# lista w postaci [value, long_j, short_j]

def get_max_value(list, n):
    F = [0]*n
    F[n-1] = 0
    for x in range(n-2, -1, -1):
        max = 0
        if x + list[x][1] < n:
            if max < F[x+list[x][1]] + list[x+list[x][1]][0]:
                max = F[x+list[x][1]] + list[x+list[x][1]][0]
        if x + list[x][2] < n:
            if max < F[x+list[x][2]] + list[x+list[x][2]][0]:
                max = F[x+list[x][2]] + list[x+list[x][2]][0]
        F[x] = max
    print(F)
    return F[0]


list = [[6, 4, 1], [2, 2, 1], [1, 5, 3], [7, 6, 3], [12, 4, 1], [5, 2, 1], [1, 2, 6]]
print(get_max_value(list, len(list)))
