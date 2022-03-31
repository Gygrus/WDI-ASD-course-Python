"""
Mówimy, że punkt (x, y) słabo dominuje punkt (x
′
, y′
) jeśli x ≤ x
′
oraz y ≤ y
′
(w szczególności
każdy punkt słabo dominuje samego siebie). Dana jest tablica P zawierająca n punktów. Proszę
zaimplementować funkcję dominance(P), która zwraca tablicę S taką, że:
1. elementami S są indeksy punktów z P,
2. dla każdego punktu z P, S zawiera indeks punktu, który go słabo dominuje,
3. S zawiera minimalną liczbę elementów.
Przykład. Dla tablicy:
P = [ (2,2), (1,1), (2.5,0.5), (3,2), (0.5,3) ]
# 0 1 2 3 4
wynikiem jest, między innymi:
S = [ 1, 4, 2 ]
"""
def binsearch(T, P, left, right, num):
    temp = (left+right)//2
    if T[temp][1] == P[num][1]:
        while temp < len(T) and T[temp][1] == P[num][1]:
            temp += 1
        return temp - 1
    elif T[temp][1] > P[num][1]:
        return binsearch(T, P, left, temp, num)
    else:
        return binsearch(T, P, temp+1, right, num)

def dominance(P):
    def quicksort1(Tab, p, r):
        def quicksort(Tab, p, r):
            while p < r:
                q = partition(Tab, p, r)
                quicksort(Tab, p, q - 1)
                p = q + 1

        def partition(Tab, p, r):
            x = Tab[r][1]
            i = p - 1
            for j in range(p, r):
                if Tab[j][1] <= x:
                    i += 1
                    Tab[i], Tab[j] = Tab[j], Tab[i]
            Tab[i + 1], Tab[r] = Tab[r], Tab[i + 1]
            return i + 1

        quicksort(Tab, p, r)

    def quicksort_for_x(Tab, P, p, r):
        def quicksort(Tab, P, p, r):
            while p < r:
                q = partition(Tab, P, p, r)
                quicksort(Tab, P, p, q - 1)
                p = q + 1

        def partition(Tab, P, p, r):
            x = P[Tab[r]][0]
            i = p - 1
            for j in range(p, r):
                if P[Tab[j]][0] <= x:
                    i += 1
                    Tab[i], Tab[j] = Tab[j], Tab[i]
            Tab[i + 1], Tab[r] = Tab[r], Tab[i + 1]
            return i + 1

        quicksort(Tab, P, p, r)

    n = len(P)
    tab_of_x = [0]*n
    tab_of_y = [0]*n
    for x in range(n):
        tab_of_y[x] = P[x]
        tab_of_x[x] = x

    quicksort_for_x(tab_of_x, P, 0, n-1)
    quicksort1(tab_of_y, 0, n-1)

    print(tab_of_x)
    print(tab_of_y)
    mark = n
    output = []
    for x in range(n):
        temp = P[tab_of_x[x]]
        best = temp[1]
        rem = x
        cur = x
        while cur+1 < n and P[tab_of_x[cur]][0] == P[tab_of_x[cur+1]][0]:
            if P[tab_of_x[cur+1]][1] < best:
                best = P[tab_of_x[cur+1]][1]
                rem = cur+1
                temp = P[tab_of_x[cur+1]]
            cur += 1
        # print(cur, rem, x, best)
        check = binsearch(tab_of_y, P, 0, n-1, tab_of_x[rem])
        if check < mark:
            mark = check
            output.append(tab_of_x[rem])

    return output


P = [ (2,2), (1,1), (2.5,0.5), (3,2), (0.5,3) ]
print(dominance(P))







