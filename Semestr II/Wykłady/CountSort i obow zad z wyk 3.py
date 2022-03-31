from random import randint


def countsort(A, k):
    C = [0]*k
    B = [0]*len(A)
    for i in range(len(A)):
        C[A[i]] += 1

    for i in range(1, k):
        C[i] += C[i-1]

    for i in range(len(A)-1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]

    for i in range(len(A)):
        A[i] = B[i]

def count_sort_obow_1(A, n, l):
    C = [0]*n
    B = [0]*n
    for i in range(n):
        C[(A[i]//l)%n] += 1

    for i in range(1, n):
        C[i] += C[i-1]

    for i in range(n-1, -1, -1):
        C[(A[i]//l)%n] -= 1
        B[C[(A[i]//l)%n]] = A[i]

    for i in range(n):
        A[i] = B[i]


def count_sort_for_range(A, n):
    count_sort_obow_1(A, n, 1)
    count_sort_obow_1(A, n, n)

t = 36
arr = [randint(0, t*t-1) for _ in range(t)]
n = len(arr)
print("Given array is")
print(*arr)

count_sort_for_range(arr, n)

print("Sorted array is")
print(*arr)