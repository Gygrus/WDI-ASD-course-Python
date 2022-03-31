n0 = 123

def subprimes_rec(n, k, depth):
    if depth == len(str(n0)):
        print(n)
        return
    subprimes_rec((n - (n % 10**k)) // 10 + (n % 10**(k-1)), k, depth + 1)
    subprimes_rec(n, k + 1, depth + 1)



#subprimes_rec(n0, 1, 0)


def subprimes_rec2(n, k=0, depth = 0):
    if n == 0:
        print(k)
        return

    #subprimes_rec2(n // 10, (n % 10)*10**depth + k, depth + 1)
    subprimes_rec2(n // 10, k*10 + n%10, depth + 1)
    subprimes_rec2(n // 10, k, depth)

subprimes_rec2(123)