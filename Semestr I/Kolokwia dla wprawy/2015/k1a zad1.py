"""
Proszę napisać program, który wczytuje liczbę naturalną A i odpowiada na pytanie: ,,czy w którymkolwiek
z systemów o podstawie 2-16, wszystkie cyfry liczby A zapisanej w tym systemie, są liczbami pierwszymi?".
"""
from math import ceil, sqrt
all_digits = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}


A = int(input("> "))

for x in range(3, 16):
    a = A
    new = ''
    while a != 0:
        if a % x < 10:
            new += str(a%x)
            a //= x
        else:
            new += all_digits[a%x]
            a //= x

    z = True
    print(new)
    for i in new:
        if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if int(i) < 2:
                z = False
                break
            if z and int(i) > 2:
                for p in range(2, ceil(sqrt(int(i))) + 1):
                    if int(i) % p == 0:
                        z = False
                        break
            if not z:
                break

    if z:
        print("istnieje, jest to system", x)
        print(new)
        break
