
def starting_point(T, t_wierszy, t_kolumn, t_sekcji):
    for x in range(9):
        for y in range(9):
            if T[x][y] != 0:
                t_w_check = True
                t_k_check = True
                t_s_check = True
                for z in range(9):
                    if t_w_check and t_wierszy[x][z] == 0:
                        #print(T[x][y], z, (x, y))
                        t_wierszy[x][z] = T[x][y]
                        #print(t_wierszy[x])
                        t_w_check = False

                    if t_k_check and t_kolumn[y][z] == 0:
                        t_kolumn[y][z] = T[x][y]
                        t_k_check = False

                    if t_s_check and t_sekcji[y//3 + 3*(x//3)][z] == 0:
                        t_sekcji[y // 3 + 3 * (x // 3)][z] = T[x][y]
                        t_s_check = False

                    if not(t_w_check or t_k_check or t_s_check):
                        break


def sudoku(T):
    t_wierszy = [[0 for _ in range(9)] for _ in range(9)]
    t_kolumn = [[0 for _ in range(9)] for _ in range(9)]
    t_sekcji = [[0 for _ in range(9)] for _ in range(9)]

    def fill(T, i, w, k):
        if w < 9:
            if i in T[w]:
                for p in range(9):
                    fill(T, i, w+1, p)
        for x in T:
           print(x)
        print(i, w, k)
        nonlocal check
        if w == 9:
            print('gówno')
            if i != 9:
                for p in range(9):
                    check = False
                    fill(T, i+1, 0, p)
            else:
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

                else:
                    return

        if not check:
            if T[w][k] != 0 or i in t_wierszy[w] or i in t_kolumn[k] or i in t_sekcji[k//3 + 3*(w//3)]:
                return
            print(i, w, k)
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

            for p in range(9):
                #if state:
                    #break
                fill(T, i, w+1, p)

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

    starting_point(T, t_wierszy, t_kolumn, t_sekcji)
    for x in t_wierszy:
        print(x)
    print()
    for x in t_kolumn:
        print(x)
    print()
    for x in t_sekcji:
        print(x)
    for x in range(9):
        check = False
        fill(T, 1, 0, x)

#T = [[0 for _ in range(9)] for _ in range(9)]
T = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

print(sudoku(T))