def get_parameter(T, t_wierszy, t_kolumn, t_sekcji):
    #print('dupa')
    for x in range(len(T)):
        for y in range(len(T)):
            #print(x, y)
            if T[x][y] != 0:
                w_check = True
                k_check = True
                s_check = True
                if T[x][y] in t_wierszy[x]:
                    w_check = False
                if T[x][y] in t_kolumn[y]:
                    k_check = False
                if T[x][y] in t_sekcji[y//3 + 3*(x//3)]:
                    s_check = False
                for z in range(len(T)):
                    #print(w_check, k_check, s_check)
                    if w_check and t_wierszy[x][z] == 0:
                        t_wierszy[x][z] = T[x][y]
                        w_check = False
                    if k_check and t_kolumn[y][z] == 0:
                        t_kolumn[y][z] = T[x][y]
                        k_check = False
                    if s_check and t_sekcji[y//3 + 3*(x//3)][z] == 0:
                        t_sekcji[y//3 + 3*(x//3)][z] = T[x][y]
                        s_check = False

                    if not(w_check or k_check or s_check):
                        break

def sudoku(T):
    t_wierszy = [[0 for _ in range(len(T))] for _ in range(9)]
    t_kolumn = [[0 for _ in range(len(T))] for _ in range(9)]
    t_sekcji = [[0 for _ in range(len(T))] for _ in range(9)]
    get_parameter(T, t_wierszy, t_kolumn, t_sekcji)
    key_parameter = True
    while key_parameter:
        key_parameter = False
        for x in range(len(T)):
            for y in range(len(T)):
                if T[x][y] == 0:
                    key_parameter = True
                    count = 0
                    for p in range(1,10):
                        if p not in t_wierszy[x] and p not in t_kolumn[y] and p not in t_sekcji[y//3 + 3*(x//3)]:
                            z = p
                            count += 1
                    if count == 1:
                        T[x][y] = z
                        get_parameter(T, t_wierszy, t_kolumn, t_sekcji)

    for x in T:
        print(x)

T = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]
t_wierszy = [[0 for _ in range(len(T))] for _ in range(9)]
t_kolumn = [[0 for _ in range(len(T))] for _ in range(9)]
t_sekcji = [[0 for _ in range(len(T))] for _ in range(9)]
# print(get_parameter(T, t_wierszy, t_kolumn, t_sekcji))
# for x in t_wierszy:
#     print(x)
sudoku(T)

