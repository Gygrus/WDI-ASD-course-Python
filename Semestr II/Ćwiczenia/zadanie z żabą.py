def frog_jump(A):
    n = len(A)
    sum = 0
    for x in range(n):
        sum += A[x]

    # F[i][j] - minimalna liczba skoków na j-tą pozycję oraz energia na tej pozycji z uwzględnieniem i pierwszych pozycji
    # pierwszy element krotki to liczba skoków, druga to pozostała energia
    F = [[[float('inf'), 0] for _ in range(n)] for _ in range(n)]
    F[0][0] = [0, A[0]]
    for x in range(1, n):
        if A[0]-x >= 0:
            F[0][x] = [1, A[0]-x]

    for i in range(1, n):
        for j in range(0, n):
            F[i][j][0] = F[i-1][j][0]
            F[i][j][1] = F[i-1][j][1]

            if j-i <= A[i]+F[i-1][i][1] and i < j:
                temp = F[i][j][0]
                F[i][j][0] = min(F[i-1][j][0], F[i-1][i][0] + 1)

                if F[i][j][0] == F[i-1][i][0] + 1 and F[i][j][0] < temp:
                    F[i][j][1] = F[i-1][i][1] + A[i] - (j-i)
                elif F[i][j][0] == F[i-1][i][0] + 1 and F[i][j][0] == temp and F[i][j][1] < F[i-1][i][1] + A[i] - (j-i):
                    F[i][j][1] = F[i - 1][i][1] + A[i] - (j - i)


    for x in F:
        print(x)
    return F[n-1][n-1][0]

A = [2,2,1,0,0,0]
print(frog_jump(A))