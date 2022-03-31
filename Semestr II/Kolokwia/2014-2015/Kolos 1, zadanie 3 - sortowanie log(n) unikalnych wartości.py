from math import log2, ceil

def insert_to_tab(T, i, value, n):
    T[n-i]  = value
    j = n-i

    while j < n-1 and T[j+1] < value:
        T[j] = T[j+1]
        j += 1

    T[j] = value



def binary_search(T, n, a, b):
    check = (b+a)//2
    while a <= b:
        if n < T[check]:
            b = check - 1
            check = (a+b)//2
        elif n > T[check]:
            a = check + 1
            check = (a+b)//2
        else:
            return check

    return False

def naj(T):
    min = T[0]
    max = T[0]
    i = len(T)%2
    while i < len(T):
        if T[i] < T[i+1]:
            if T[i] < min:
                min = T[i]
            if T[i+1] > max:
                max = T[i+1]
        else:
            if T[i] > max:
                max = T[i]
            if T[i+1] < min:
                min = T[i+1]
        i += 2

    return min, max




def sort_log(T):
    min, max = naj(T)
    n = int(ceil(log2(len(T))))
    elem = [min-1]*n
    index_tab = [0]*n
    result = [0]*len(T)
    elem[n-1] = max
    elem[n-2] = min
    i = 3
    for x in range(len(T)):
        if not binary_search(elem, T[x], 0, n-1):
            insert_to_tab(elem, i, T[x], n)
            i += 1
            if i == n+1:
                break

    for x in range(len(T)):
        index = binary_search(elem, T[x], 0, n-1)
        index_tab[index] += 1

    for x in range(1, len(elem)):
        index_tab[x] += index_tab[x-1]


    for x in range(len(T)-1, -1, -1):
        index = binary_search(elem, T[x], 0, n-1)
        index_tab[index] -= 1
        result[index_tab[index]] = T[x]

    for x in range(len(T)):
        T[x] = result[x]



T = [-37, -37, 12, 5, 12, 12, 5, -37, 5, 5, 5, 14, 14, 14, 14]
sort_log(T)
print(T)
