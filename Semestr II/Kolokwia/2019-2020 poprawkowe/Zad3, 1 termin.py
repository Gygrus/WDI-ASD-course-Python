"""
Dana jest tablica A zawierająca n = len(A) liczb naturalnych. Dodatkowo wiadomo, że A w sumie
zawiera k różnych liczb (należy założyć, że k jest dużo mniejsze niż n). Proszę zaimplementować
funkcję longest incomplete(A, k), która zwraca długość najdłuższego spójnego ciągu elementów
z tablicy A, w którym nie występuje wszystkie k liczb. (Można założyć, że podana wartość k jest
zawsze prawidłowa.)
Przykład Dla tablicy
A = [1,100, 5, 100, 1, 5, 1, 5]
wartością wywołania longest incomplete(A, 3) powinno być 4 (ciąg 1, 5, 1, 5 z końca tablicy).
"""

def find_and_change(tab, num, left, right, mode, unique):
    mark = (left + right)//2
    if tab[mark][0] == num:
        if mode == 1 and tab[mark][1] == 0:
            unique += 1
        elif mode == 0 and tab[mark][1] == 1:
            unique -= 1
        tab[mark][1] += (-1)**(mode+1)
        return unique
    elif tab[mark][0] > num:
        return find_and_change(tab, num, left, mark, mode, unique)
    else:
        return find_and_change(tab, num, mark+1, right, mode, unique)


def longest_incomplete(A, k):
    n = len(A)
    tab_of_numbers = [[-1, 0] for _ in range(k)]
    counter = 0
    for x in range(n):
        if counter == k:
            break
        check = False
        for y in range(k):
            if A[x] == tab_of_numbers[y][0]:
                check = True
                break
        if not check:
            for y in range(k):
                if tab_of_numbers[y][0] == -1:
                    tab_of_numbers[y][0] = A[x]
                    counter += 1
                    break

    tab_of_numbers = sorted(tab_of_numbers, key=lambda x: x[0])
    a = 0
    b = 0
    for i in range(k):
        if A[0] == tab_of_numbers[i][0]:
            tab_of_numbers[i][1] += 1
            break

    best = 1
    unique = 1
    while b != n-1:
        if unique < k:
            b += 1
            temp = A[b]
            unique = find_and_change(tab_of_numbers, temp, 0, k-1, 1, unique)
        else:
            temp = A[a]
            best = max(best, b - a)
            unique = find_and_change(tab_of_numbers, temp, 0, k-1, 0, unique)
            a += 1

    if unique < k and b-a+1 > best:
        best = b-a+1
        return best

    while a != b:
        temp = A[a]
        best = max(best, b - a)
        unique = find_and_change(tab_of_numbers, temp, 0, k-1, 0, unique)
        a += 1


    return best

A = [1,100, 5, 100, 1, 5, 1, 5]
print(longest_incomplete(A, 3))
