from random import shuffle

def find_cycle_of_4(graph):
    n = len(graph)
    F = [[-1 for _ in range(n)] for _ in range(n)]
    print(n)
    for x in range(n):
        for y in range(n):
            if graph[x][y]:
                for z in range(y+1, n):
                    if graph[x][z]:
                        if F[y][z] != -1:
                            return [y, F[y][z], z, x]
                        else:
                            F[y][z] = x


    print("There are no cycles of length 4!")
    return

graph = [[4], [2, 8], [3, 4, 1], [5, 6, 8, 2], [2, 0, 7], [3, 6, 8], [5, 3], [4, 8], [3, 5, 7, 1]]
a = [4]
b = [2, 8]
c = [3, 4, 1]
d = [5, 6, 8, 2]
e = [2, 0, 7]
f = [3, 6, 8]
g = [5, 3]
h = [4, 8]
i = [3, 5, 7, 1]
g1 = [[0,0,0,0,1,0,0,0,0],
      [0,0,1,0,0,0,0,0,1],
      [0,1,0,1,1,0,0,0,0],
      [0,0,1,0,0,1,1,0,1],
      [1,0,1,0,0,0,0,1,0],
      [0,0,0,1,0,0,1,0,1],
      [0,0,0,1,0,1,0,0,0],
      [0,0,0,0,1,0,0,0,1],
      [0,1,0,1,0,1,0,1,0]]
shuffle(a)
shuffle(b)
shuffle(c)
shuffle(d)
shuffle(e)
shuffle(f)
shuffle(g)
shuffle(h)
shuffle(i)
graph = [a, b, c, d, e, f, g, h, i]
# graph = [[4, 1], [0, 2], [4, 3, 1], [5, 6], [2, 7, 0], [6, 3], [3, 5], [4]]
g2 = [[1, 4, 3], [4, 0, 5], [3, 5], [2, 0], [0, 1], [1, 2]]
print(graph)
print(find_cycle_of_4(g1))