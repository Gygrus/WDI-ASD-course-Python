"""
Given a rod of length n inches and an array of prices that contains prices of all pieces of
size smaller than n. Determine the maximum value obtainable by cutting up the
rod and selling the pieces.
"""

def bottom_up_cut_rod(p, n):
    T = [0]*(n+1)
    T[0] = 0
    for i in range(1, n+1):
        q = -999999
        for j in range(1, i+1):
            q = max(q, p[j] + T[i-j])

        T[j] = q

    return T[n]

def bottom_up_ze_zwracaniem(p, n):
    T = [0] * (n + 1)
    mem = [0]*(n+1)
    T[0] = 0
    for i in range(1, n + 1):
        q = -999999
        for j in range(1, i + 1):
            if p[j] + T[i-j] > q:
                q = p[j] + T[i-j]
                mem[i] = j

        T[j] = q

    return (T, mem)

def getsolution(T, n, mem):
    i = n
    while n != 0:
        print(mem[n])
        i -= mem[n]
        n = i


p = [0, 1, 5, 8, 9, 10, 17, 17, 20]
a, b = bottom_up_ze_zwracaniem(p, 8)
print(a)
print(b)
print(getsolution(a, 8, b))
