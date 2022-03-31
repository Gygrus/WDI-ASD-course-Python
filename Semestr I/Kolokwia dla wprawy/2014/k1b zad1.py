"""
1. Proszę napisać program, który wczytuje wprowadzany z klawiatury ciąg liczb naturalnych
zakończonych zerem stanowiącym wyłącznie znacznik końca danych.
Program powinien wypisać te elementy ciągu które są równe średniej arytmetycznej z 4 najbliższych
sąsiadów. Na przykład dla ciągu: 2,3,2,7,1,2,4,8,5,2,2,4,3,9,5,4,0 powinny zostać wypisane
podkreślone liczby. Można założyć, że w ciągu znajduje się co najmniej 5 elementów
"""
tab = [0]*5
while True:
    n = int(input("> "))
    if n == 0:
        break
    for x in range(len(tab)):
        temp = tab[x]
        tab[x] = n
        n = temp
    print(tab)
    suma = 0

    for x in tab:
        suma += x

    for p in range(len(tab)):
        if tab[p] == (suma - tab[p]) / 4:
            print(tab[p])





