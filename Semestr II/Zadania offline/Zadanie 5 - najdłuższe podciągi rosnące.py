"""
Proszę zaimplementować funkcję printAllLIS( A ), która otrzymuje na wejściu tablicę liczb naturalnych A i wypisuje na ekran wszystkie najdłuższe ciągi
rosnące oraz zwraca ich liczbę. Na przykład dla tablicy
A = [2,1,4,3]
wynikiem powinno być wypisanie (z dokładnością do kolejności ciągów):
2 4
2 3
1 4
1 3
oraz zwrócenie liczby 4.
"""
from random import randint
from time import time

def printAllLIS(A):                                         #główna funkcja
    def LIS(A, n):                                   #funkcja LIS, zwróci nadłuższy rosnący podciąg, tablicę P (na które indeksy trzeba iść z
                                                     #z elementu, żeby natrafić na kolejne elementy najdłuższego podciągu) oraz F (długość najdłuższego podciągu rosnącego
                                                     #zaczynającego się od elementu pod podanym indeksem)
        F = [1]*n
        P = [[]]*n
        for i in range(n-2, -1, -1):
            for j in range(n-1, i, -1):
                if A[j] > A[i]:
                    if F[j]+1 > F[i]:
                        F[i] = F[j]+1
                        P[i] = [j]                   #jeśli pod indeksem i zwiększamy długość najdłuższego podciągu,
                                                     #to ustawiamy wartość pod P[i] jako [j], bo tylko na pozycję pod indeksem j-tym
                                                     #możemy się udać, aby przejść do kolejnego elementu rosnącego podciągu
                    elif F[j]+1 == F[i]:
                        P[i].append(j)               #jeśli wyrównujemy długość najdłuższego rosn. podc. pod indeksem i-tym, to
                                                     #do P[i] dodajemy kolejny indeks, do którego można się przemieścić (alternatywnie
                                                     #do już będącego w P[i] indeksu


        return (max(F), F, P)                        #zwracamy długość LIS, tablicę LIS-ów od poszczególnych indeksów tablicy, oraz tablicę
                                                     #indeksów do których trzeba się przemieścić, chcąc wypisać LIS-y od poszczególnych indeksów

    def printsolution(A, P, i, help_tab, k):         #rekurencyjna funkcja wypisująca LIS-y
        help_tab[k] = A[i]                           #help_tab to pomocnicza tablica, w której przechowuje elementy LIS-ów
        if P[i]:                                     #jeśli można przejść dalej z pozycji i-tej:
            for x in range(len(P[i])-1, -1, -1):                    #iteruję po wszystkich możliwych indeksach, do których mogę przejść
                                                                    #(od tyłu, dla zachowania odpowiedniej kolejności)
                printsolution(A, P, P[i][x], help_tab, k+1)         #kolejne wywołanie rekurencyjne
        else:
            nonlocal counter                         #w przeciwnym razie po prostu zwiększam ilość LIS-ów (w counterze) i wypisuje LIS-a
            counter += 1
            for x in range(len(help_tab)):
                print(help_tab[x], end=' ')
            print()

    n = len(A)                                      #długość tablicy wejściowej
    result, F, P = LIS(A, n)                        #przypisanie długości LIS-a, tablicy F oraz P

    counter = 0                                     #zwracana na długość ilość LIS-ów na początku równa 0
    help_tab = [0]*result                           #pomocnicza tablica na elementy poszczególnych LIS-ów
    for x in range(n):                              #iteruję po indeksach tablicy A, jeśli pod danym indeksem
                                                    #długość LIS-a jest równa długości najdłuższego LIS-a (result)
                                                    #to wypisuję dany podciąg
        if F[x] == result:
            printsolution(A, P, x, help_tab, 0)

    return counter                                  #na końcu zwracam ilość znalezionych LIS-ów





A = [10*k+i for k in range(8) for i in range(6,0,-1)]
print(A)
start1 = time()
print(printAllLIS(A))
end1 = time()
print("Moje: ", end1-start1)
