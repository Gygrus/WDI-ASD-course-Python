from random import randint, seed
from time import time

seed(422)
def quicksort1(Tab, p, r):
    def quicksort(Tab, p, r):
        while p < r:
            q = partition(Tab, p, r)
            quicksort(Tab, p, q-1)
            p = q + 1

    def partition(Tab, p, r):
        x = Tab[r]
        i = p-1
        for j in range(p, r):
            if Tab[j] <= x:
                i += 1
                Tab[i], Tab[j] = Tab[j], Tab[i]
        Tab[i+1], Tab[r] = Tab[r], Tab[i+1]
        return i+1

    quicksort(Tab, p, r)

def quicksort_boosted(T, p, r):
    while p < r:
        q = partition_boosted(T, p, r)
        if q - p < r - q:
            quicksort_boosted(T, p, q-1)
            p = q + 1
        else:
            quicksort_boosted(T, q+1, r)
            r = q - 1


def partition_boosted(Tab, p, r):
    if r-p >1:
        a = randint(p, r)
        Tab[a], Tab[r] = Tab[r], Tab[a]

    x = Tab[r]
    i = p-1
    for j in range(p, r):
        if Tab[j] < x:
            i += 1
            Tab[i], Tab[j] = Tab[j], Tab[i]
    Tab[i+1], Tab[r] = Tab[r], Tab[i+1]
    return i+1




def getdata(n):
    return [randint(-100000, 100000) for i in range(n)]

n = int(input("> "))
T = getdata(n)
print(n)

start = time()

quicksort1(T, 0, n-1)
end = time()
print("Wynik =", T)


print("Czas działania: %f sek." % (end - start))