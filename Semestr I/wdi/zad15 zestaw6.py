def collides(positions, upto):
    N = len(positions)
    rows = [False]*N
    cols = [False]*N
    diags_down = [False] * (N * 2 - 1)
    diags_up = [False] * (N * 2 -1)

    for r in range(N):
        row = r
        col = positions[r]
        diags_up = row+col
        diag_down = (N - 1 - row) + col

    if rows[row]:
        return False

    rows[row] = True

    if cols[col]:
        return False


def zad15(positions, row):
    N = len(positions)
    for i in range(N):
        positions[row] = i
        zad15(positions, row+1)



N = 8
positions = [0]*N
zad15(positions, 0)

board = [[0 for _ in range(N)] for _ in range(N)]
for r in range(N):
    board[r][positions[r]] = 1

for row in board:
    for c in row:
        print(c, end='\t')
    print()