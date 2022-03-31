"""
W problemie sumy podzbiorów mamy dany ciąg liczb dodatnich A[0], ..., A[n-1] oraz liczbę T.
Należy stwierdzić, czy istnieje podciąg sumujący się dokładnie do T.
"""
"""
Wiersze tablicy F[i][j] odpowiadają kolejnym liczbom w tablicy A, a kolumny to odpowiednie sumy.
Pozycja F[i][j] odpowiada na pytanie, czy dla liczb od 0 do i-tej można znaleźć sumę j."""

def check_if_exists(A, T):
    n = len(A)
    F = [True]*(n)
    for i in range(n):
        F[i] = [False]*(T+1)


    #F[0][A[0]] = True

    for i in range(n):
        F[i][0] = True

    # for sum in range(T+1):
    #     if sum == A[0]:
    #         F[0][sum] = True
    #         break
    F[0][A[0]] = True
    # for sum in range(1, T+1):
    #     F[0][sum] = False

    for i in range(1, n):
        for j in range(1, T+1):
            F[i][j] = F[i-1][j]
            if A[i] <= j:
                F[i][j] = (F[i][j] or F[i-1][j-A[i]])

    for i in range(n):
        for j in range(T + 1):
            print (F[i][j], end =" ")
        print()


    return F[n-1][T]


T = [3, 4, 5, 2, 7, 8]
print(check_if_exists(T, 29))