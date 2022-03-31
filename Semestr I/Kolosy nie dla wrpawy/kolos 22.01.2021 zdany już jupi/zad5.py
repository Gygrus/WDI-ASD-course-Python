#Piotr Socała
# (stworzenie f-cji pomocniczej sprawdzającej NWD)
# przeiteruję po kolejnych elementach tablicy
# i będę rozpatrywał wszystkie możliwe możliwości
# w 3 pętlach for
#


def check_NWD(a, b, c):
    if a == 1 or b == 1 or c == 1:
        return 1
    first = 0
    second = 0
    third = 0
    i = 2
    while i <= a and i <= b:
        if a % i == 0 and b % i == 0:
            first = i
            break
        i += 1
    if first == 0:
        first = 1
    i = 2
    while i <= a and i <= c:
        if a % i == 0 and c % i == 0:
            second = i
            break
        i += 1
    if second == 0:
        second = 1

    i = 2
    while i <= b and i <= c:
        if b % i == 0 and c % i == 0:
            second = i
            break
        i += 1
    if third == 0:
        third = 1

    if first == second == third == 1:
        return True

    return False

#end def


def trojki(T):
    k = len(T)
    counter = 0
    for x in range(k-2):
        for y in range(x+1, x+3):
            if y <= k-2:
                for z in range(y+1, y+3):
                    if z > k-1:
                        break
                    if check_NWD(T[x], T[y], T[z]):
                        counter += 1

    return counter
#end def


