"""
Napisać program wczytujący dwie liczby naturalne i odpowiadający
na pytanie czy są one zbudowane z takich samych cyfr, np. 123 i
321, 1255 i 5125, 11000 i 10001.
"""

x = input("pierwsza liczba")
y = input("druga liczba")
z = True
x_1 = [i for i in x]
y_1 = [i for i in y]
if len(x) == len(y):
    for k in x:
        if k not in y_1:
            z = False
            break
        else:
            y_1.remove(k)

    for k in y:
        if k not in x_1:
            z = False
            break
        else:
            x_1.remove(k)
    if z:
        print("Mają takie same liczby")