"""
A - dodaje do liczby 3
B - mnoży przez 2
C - zamienia miejscami dwie ostatnie cyfry
Czy da się w maksymalnie k krokach uzyskać liczbę pierwszą?
"""

def check_if_prime(n):
    if n <= 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1

    return True

def execute_c(n):
    x = n % 10
    y = (n%100) // 10
    n //= 100
    return n*100 + 10*x + y



def rekur(n, i, k, order = ''):
    #print(order, n)
    if check_if_prime(n):
        check = True
        print(order)
        return True

    if i == k:
        return False

    A_case = n+3
    B_case = 2*n
    C_case = execute_c(n)

    return rekur(A_case, i+1, k, order + 'A') or rekur(B_case, i+1, k, order + 'B') or rekur(C_case, i+1, k, order + 'C')

print(rekur(18, 0, 3))

