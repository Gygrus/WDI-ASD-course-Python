def skok(T, x, y, licznik):
    T[x][y] = licznik
    n = len(T)
    if licznik == n*n:
        return True
    positions = [(x + 1, y + 2), (x + 1, y - 2),
                 (x - 1, y + 2), (x - 1, y - 2),
                 (x + 2, y + 1), (x + 2, y - 1),
                 (x - 2, y + 1), (x - 2, y - 1)]
    for i in range(8):
        if positions[i][0] >= 0 and positions[i][0] < n and positions[i][1] >= 0 and positions[i][1] < n and T[positions[i][0]][positions[i][1]] == 0:
            if skok(T, positions[i][0], positions[i][1], licznik+1):
                return True
    T[x][y] = 0
    return False


T = [[0]*8 for i in range(8)]
for x in T:
    print(x)
print(skok(T, 0, 0, 1))
