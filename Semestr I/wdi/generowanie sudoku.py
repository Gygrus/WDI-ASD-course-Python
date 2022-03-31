def sudoku(T):
    t_wierszy = [[0 for _ in range(9)] for _ in range(9)]
    t_kolumn = [[0 for _ in range(9)] for _ in range(9)]
    t_sekcji = [[0 for _ in range(9)] for _ in range(9)]
    check = False

    def fill(T, i, w, k):
        nonlocal check
        if w == 9:
            if i != 9:
                for p in range(9):
                    fill(T, i+1, 0, p)
            state = True
            for x in T:
                if 0 in x:
                    state = False
                    break

            if state:
                for x in T:
                    print(x)
                check = True
                print()
                #print()
                #check = True
        if not check:
            if T[w][k] != 0 or i in t_wierszy[w] or i in t_kolumn[k] or i in t_sekcji[k//3 + 3*(w//3)]:
                return
            T[w][k] = i
            w_check = True
            k_check = True
            s_check = True
            for x in range(9):
                if w_check:
                    if t_wierszy[w][x] == 0:
                        t_wierszy[w][x] = i
                        w_check = False
                if k_check:
                    if t_kolumn[k][x] == 0:
                        t_kolumn[k][x] = i
                        k_check = False
                if s_check:
                    if t_sekcji[k//3 + 3*(w//3)][x] == 0:
                        t_sekcji[k//3 + 3*(w//3)][x] = i
                        s_check = False

                if not(w_check or s_check or k_check):
                    break

            for x in range(9):
                fill(T, i, w+1, x)

            for x in range(8, -1, -1):
                if not w_check:
                    if t_wierszy[w][x] != 0:
                        t_wierszy[w][x] = 0
                        w_check = True
                if not k_check:
                    if t_kolumn[k][x] != 0:
                        t_kolumn[k][x] = 0
                        k_check = True
                if not s_check:
                    if t_sekcji[k//3 + 3*(w//3)][x] != 0:
                        t_sekcji[k//3 + 3*(w//3)][x] = 0
                        s_check = True

                if w_check and s_check and k_check:
                    break

            T[w][k] = 0
    for x in range(9):
        check = False
        fill(T, 1, 0, x)