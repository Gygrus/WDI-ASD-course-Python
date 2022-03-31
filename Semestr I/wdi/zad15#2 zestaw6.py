'''Problem 8 Hetmanów (treść oczywista)'''


def hetmany(N):
    t = [-1 for _ in range(N)]
    t0 = [False for _ in range(2*N - 1)]
    t1 = [False for _ in range(2*N - 1)]
    t2 = [False for _ in range(2*N - 1)]
    stop_func = False

    def hetman(w, k):
        nonlocal stop_func
        if w == N:
            rysuj(t)
            stop_func = True
        if t0[k] or t1[w + k] or t2[N - 1 + k - w]:
            return
        t0[k] = t1[w+k] = t2[N-1+k-w] = True
        t[w] = k
        for i in range(N):
            if stop_func:
                return
            if w+1 == N and i >0:
                break
            hetman(w+1, i)
        t0[k] = t1[w + k] = t2[N - 1 + k - w] = False

    def rysuj(tab):
        for i in range(len(tab)):
            for j in range(len(tab)):
                if t[i] == j:
                    print("X", end=' ')
                else: print(". ", end='')
            print()
        print()

    for x in range(N):
        hetman(0, x)

# end def


hetmany(9)
print("Do widzenia")