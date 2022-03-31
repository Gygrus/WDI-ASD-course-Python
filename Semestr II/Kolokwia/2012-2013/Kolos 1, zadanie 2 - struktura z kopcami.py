"""
Proszę zaprojektowac strukturę danych przechowującą liczby i pozwalającą na następujące
operacje (zakładamy, że wszystkie liczby umieszczane w strukturze są różne):
Init(n). Tworzy zadaną strukturę danych zdolną pomieścić maksymalnie n liczb.
Insert(x). Dodaje do struktury liczbę x.
RemoveMin() Znajduje najmniejszą liczbę w strukturze, usuwa ją i zwraca jej wartość.
RemoveMax() Znajduje największą liczbę w strukturze, usuwa ją i zwraca jej wartość.
Każda z operacji powinna mieć złożoność O(log n, gdzie n to ilość liczb znajdujących się obecnie
w strukturze. W tym zadaniu nie trzeba implementować podanych operacji, a jedynie
przekonująco opisać jak powinny być zrealizowane i dlaczego mają wymaganą złożoność.
"""


"""
Zastosuję w strukturzę kopiec min i kopiec max, przechowując w obu kopcach wszystkie wartości oraz ich indeksy zarówno
w jednym jak i drugim kopcu."""
from random import randint, shuffle

def parent(i):
    return (i-1)//2

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def minHeapify(A, B, n, i):
    l = left(i)
    r = right(i)
    m = i
    if l < n and A[l] < A[m]:
        m = l

    if r < n and A[r] < A[m]:
        m = r

    if m != i:
        A[m], A[i] = A[i], A[m]
        B[A[i][1]][1] = i
        B[A[m][1]][1] = m
        minHeapify(A, B, n, m)


def maxHeapify(A, B, n, i):
    l = left(i)
    r = right(i)
    m = i
    if l < n and A[l] > A[m]:
        m = l

    if r < n and A[r] > A[m]:
        m = r

    if m != i:
        A[m], A[i] = A[i], A[m]
        B[A[i][1]][1] = i
        B[A[m][1]][1] = m
        maxHeapify(A, B, n, m)



def Init(A, n):
    minheap = [[0, 0] for _ in range(n)]
    maxheap = [[0, 0] for _ in range(n)]

    for x in range(n):
        minheap[x][0] = A[x]
        minheap[x][1] = x
        maxheap[x][0] = A[x]
        maxheap[x][1] = x

    for x in range(parent(n-1), -1, -1):
        minHeapify(minheap, maxheap, n, x)
        maxHeapify(maxheap, minheap, n, x)

    return minheap, maxheap


def RemoveMin(minheap, maxheap, n):
    minheap[0], minheap[n-1] = minheap[n-1], minheap[0]
    min = minheap.pop()
    minHeapify(minheap, maxheap, n-1, 0)
    maxheap[min[1]], maxheap[n-1] = maxheap[n-1], maxheap[min[1]]
    if min[1] != n-1 and maxheap[min[1]][1] != n-1:
        minheap[maxheap[min[1]][1]][1] = min[1]
    maxheap.pop()
    maxHeapify(maxheap, minheap, n-1, min[1])
    return min[0]



def RemoveMax(minheap, maxheap, n):
    maxheap[0], maxheap[n - 1] = maxheap[n - 1], maxheap[0]
    max = maxheap.pop()
    maxHeapify(maxheap, minheap, n - 1, 0)
    minheap[max[1]], minheap[n - 1] = minheap[n - 1], minheap[max[1]]
    if max[1] != n - 1 and minheap[max[1]][1] != n-1:
        maxheap[minheap[max[1]][1]][1] = max[1]
    minheap.pop()
    minHeapify(minheap, maxheap, n - 1, max[1])
    return max[0]


def Insert(minheap, maxheap, x, n):
    minheap.append([x, n])
    maxheap.append([x, n])
    k = n
    while k >= 1 and minheap[parent(k)][0] > x:
        minheap[k] = minheap[parent(k)]
        maxheap[minheap[k][1]][1] = k
        k = parent(k)

    minheap[k] = [x, n]
    new = k

    k = n
    while k >= 1 and maxheap[parent(k)][0] < x:
        maxheap[k] = maxheap[parent(k)]
        maxheap[maxheap[k][1]][1] = k
        k = parent(k)

    maxheap[k] = [x, new]
    minheap[new][1] = k

T = list(range(9))
shuffle(T)
minheap, maxheap = Init(T, len(T))
print(minheap)
print(maxheap)
# for x in range(len(T)//2):
#     #print("Start!")
#     RemoveMax(minheap, maxheap, len(minheap))
#     #print(minheap)
#     #print(maxheap)
#     RemoveMin(minheap, maxheap, len(minheap))
#     #print(minheap)
#     #print(maxheap)
#     #print("Stop!")

Insert(minheap, maxheap, 18, len(minheap))
print(minheap)
print(maxheap)
Insert(minheap, maxheap, 13, len(minheap))
print(minheap)
print(maxheap)
Insert(minheap, maxheap, 14, len(minheap))
print(minheap)
print(maxheap)
Insert(minheap, maxheap, 10, len(minheap))
print(minheap)
print(maxheap)



# k = RemoveMin(minheap, maxheap, len(minheap))
# # print(k)
# print(minheap)
# print(maxheap)
# k = RemoveMin(minheap, maxheap, len(minheap))
# # print(k)
# print(minheap)
# print(maxheap)
# k = RemoveMax(minheap, maxheap, len(maxheap))
# print(minheap)
# print(maxheap)
# k = RemoveMax(minheap, maxheap, len(maxheap))
# print(minheap)
# print(maxheap)

