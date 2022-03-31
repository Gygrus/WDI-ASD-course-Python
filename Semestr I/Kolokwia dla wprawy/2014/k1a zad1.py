"""
 Proszę napisać program, który wczytuje wprowadzany z klawiatury ciąg liczb naturalnych
zakończonych zerem stanowiącym wyłącznie znacznik końca danych.
Program powinien wypisać 10 co do wielkości wartość, jaka wystąpiła w ciągu.
Na przykład dla ciągu: 1,2,3,2,3,4,5,6,7,8,9,9,11,12,13,0 powinna zostać wypisana liczba 3.
Można założyć, że w ciągu znajduje się wystarczająca liczba elementów.
"""

tab = [0]*10
while True:
    n = int(input("> "))
    if n == 0:
        print(tab, tab[9])
        break

    temp = n
    for x in range(len(tab)):
        if n > tab[x]:
            temp = tab[x]
            tab[x] = n
            n = temp
        if n == 0:
            break

