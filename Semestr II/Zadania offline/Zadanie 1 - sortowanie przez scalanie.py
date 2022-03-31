from time import time
from random import seed, randint
from sys import argv

seed(42)

def mergesort(T):

    def merge(t1, t2):
        n, m = len(t1), len(t2)
        i = j = 0
        result = list()
        while i < n and j < m:
            if t1[i]<t2[j]:
                result.append(t1[i])
                i += 1
            else:
                result.append(t2[j])
                j += 1
        if i >= n and j < m:
            result = result + t2[j:m]
        elif i < n and j >= m:
            result = result + t1[i:n]

        return result

    def rekur(T, a, b):
        n = b - a + 1
        m = a + (b - a) // 2
        if n == 2:
            if T[a] < T[b]:
                return [T[a], T[b]]
            else:
                return [T[b], T[a]]
        if n == 1:
            return [T[a]]

        result1 = rekur(T, a, m)
        result2 = rekur(T, m+1, b)

        return merge(result1, result2)

    return rekur(T, 0, len(T)-1)


def getdata(n):
    return [randint(-100000, 100000) for i in range(n)]

n = int(input("> "))
T = getdata(n)
print(n)

start = time()

result = mergesort(T)
print("Wynik =", result)

end = time()

print("Czas działania: %f sek." % (end - start))

#print(mergesort([6]))