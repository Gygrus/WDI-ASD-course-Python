from random import randint
"""RadixSort dla liczb w n elementowej tablicy o elementach z zakresu 0, n^2-1"""

def countsort(A, n, l):
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





def radixsort(A):
    n = len(A)
    countsort(A, n, 1)
    countsort(A, n, n)


t = 36
arr = [randint(0, t*t-1) for _ in range(t)]
n = len(arr)
print("Given array is")
print(*arr)

radixsort(arr)

print("Sorted array is")
print(*arr)
