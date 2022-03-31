"""
Dana jest tablica int t[N][N] zawierająca liczby naturalne. Dokładnie w jednym
wierszu, bądź kolumnie znajduje się fragmentu ciągu arytmetycznego o długości
większej niż 2, którego elementy są liczbami pierwszymi. Proszę napisać funkcję
która zwróci długość tego ciągu
"""
from random import randint


def check_if_prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True
print(check_if_prime(4))
def find_arith(t):
    result = 0
    for x in range(len(t)):
        r_poz = t[x][0] - t[x][1]
        counter_poz = 0
        r_pion = t[0][x] - t[1][x]
        counter_pion = 0
        for y in range(len(t)-1):
            print(x, y, t[x][y], t[x][y+1], (r_poz, t[x][y] - t[x][y+1]), check_if_prime(t[x][y]), check_if_prime(t[x][y+1]))
            if check_if_prime(t[x][y]) and check_if_prime(t[x][y+1]):
                if t[x][y] - t[x][y+1] == r_poz:
                    if counter_poz == 0:
                        counter_poz = 2
                    #print('hura', x, y, 'poziom')
                    else:
                        counter_poz += 1
                else:
                    counter_poz = 2

            else:
                counter_poz = 0

            r_poz = t[x][y] - t[x][y+1]

            if check_if_prime(t[y][x]) and check_if_prime(t[y+1][x]):
                if t[y][x] - t[y+1][x] == r_pion:
                    if counter_pion == 0:
                        counter_pion = 2
                    else:
                        print('hura', x, y, 'pion')
                        counter_pion += 1
                else:
                    counter_pion = 2

            else:
                counter_pion = 0

            r_pion = t[y][x] - t[y+1][x]

            if counter_poz > 2 and counter_poz > result:
                print('hura', x, y)
                result = counter_poz
            elif counter_pion > 2 and counter_pion > result:
                result = counter_pion

        if result > 0:
            return result


t = [[randint(1, 2) for _ in range(8)] for _ in range(8)]
# t = [[2, 2, 2, 2, 2, 2, 1, 2],
# [2, 1, 1, 2, 2, 1, 1, 2],
# [1, 2, 2, 1, 1, 2, 2, 1],
# [2, 2, 1, 1, 1, 2, 1, 1],
# [1, 1, 1, 1, 2, 1, 1, 1],
# [2, 1, 1, 1, 1, 1, 1, 1],
# [1, 1, 1, 2, 1, 1, 2, 2],
#[1, 2, 1, 1, 2, 1, 2, 2]]
for x in t:
    print(x)

print(find_arith(t))

