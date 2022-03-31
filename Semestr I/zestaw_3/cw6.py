"""
Proszę napisać program, który wczytuje wprowadzany z klawiatury
ciąg liczb naturalnych zakończonych zerem stanowiącym wyłącznie
znacznik końca danych. Program powinien wypisać 10 co do
wielkości wartość, jaka wystąpiła w ciągu. Można założyć, że w
ciągu znajduje się wystarczająca liczba elementów.

"""

x = input()

x = x.split(" ")
z = len(x)

p = x
nowa = []
while len(nowa) != z - 1:
    i = 0
    maks = 0
    while i < len(p):
        if int(p[i]) > maks:
            maks = int(p[i])
        i += 1
    nowa.append(maks)
    p.remove(str(maks))
print(nowa)
print(nowa[9])
