"""Dwie liczby naturalne s¡ ró»nocyfrowe, je»eli nie posiadaj¡ »adnej wspólnej cyfry. Prosz¦ napisa¢ program,
który wczytuje dwie liczby naturalne i poszukuje najmniejszej podstawy systemu (w zakresie 2-16), w którym
liczby s¡ ró»nocyfrowe. Program powinien wypisa¢ znalezion¡ podstaw¦; je»eli podstawa taka nie istnieje,
nale»y wypisa¢ komunikat o jej braku.
Na przykªad: dla liczb 123 i 522 odpowiedzi¡ jest podstawa 11, bo 123(10) = 102(11) i 522(10) = 435(11)
"""

x = int(input("> "))
y = int(input("> "))


n = 2
k = True
all_numbers = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}
while n < 17:
    new_x = ''
    x_1 = x
    while x_1 != 0:
        new_x += all_numbers[x_1 % n]
        x_1 = x_1 // n


    new_y = ''
    y_1 = y
    while y_1 != 0:
        new_y += all_numbers[y_1 % n]
        y_1 = y_1 // n

    z = False
    for p in new_x:
        if p in new_y:
            z = True
            break

    if z == False:
        print("podstawa", n, new_x, " ", new_y)
        break

    n += 1

if z:
    print("Nie ma")


