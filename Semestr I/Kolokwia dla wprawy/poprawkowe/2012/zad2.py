"""
Napisz procedurę, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie co najmniej
dwucyfrowe liczby pierwsze, powstale poprzez wykreślenie z liczby pierwotnej co najmniej jednej cyfry.
"""
def check_if_prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1

    return True

def get_length(n):
    copy = n
    length = 0
    while copy != 0:
        length += 1
        copy //= 10
    return length


def write_all(n):
    copy = n
    length = 0
    while copy != 0:
        length += 1
        copy //= 10

    tab = [0]*length
    copy = n
    i = 0
    while copy != 0:
        tab[i] = copy // 10**(length-1)
        copy = copy % 10**(length-1)
        length -= 1
        i += 1

    print(tab)
    def rekur(tab, new, i):
        if i == len(tab):
            if check_if_prime(new) and get_length(new) > 1 and get_length(new) < len(tab):
                print(new)

            return

        rekur(tab, new*10 + tab[i], i+1)
        rekur(tab, new, i+1)

    rekur(tab, 0, 0)


write_all(125623)