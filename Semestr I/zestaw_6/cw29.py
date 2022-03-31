"""
Punkt leżący w przestrzeni jest opisywany trójką liczb typu float (x,y,z). Tablica T[N] zawiera
współrzędne N punktów leżących w przestrzeni. Punkty posiadają jednostkową masę. Proszę napisać funkcję,
która sprawdza czy istnieje podzbiór punktów liczący co najmniej 3 punkty, którego środek ciężkości leży w
odległości nie większej niż r od początku układu współrzędnych. Do funkcji należy przekazać tablicę T oraz
promień r, funkcja powinna zwrócić wartość typu bool.
"""
from math import sqrt

def rekur(T, r):

    def check_distance(pupa):
        print(sqrt(pupa[0]**2 + pupa[1]**2 + pupa[2]**2))
        return sqrt(pupa[0]**2 + pupa[1]**2 + pupa[2]**2)

    def find_subsets(T, x, y, z, count, i, r):
        if i == len(T):
            if count >= 3:
                if check_distance((x/count, y/count, z/count)) == r:
                    return True
                else:
                    return False

        else:
            return find_subsets(T, x, y, z, count, i+1, r) or find_subsets(T, x+T[i][0], y+T[i][1], z+T[i][2], count+1, i+1, r)

    if find_subsets(T, 0, 0, 0, 0, 0, r):
        return True
print(sqrt(3))

print(rekur([[1, 1, 1], [1, 1, 1], [2, 3, 6], [1, 1, 1]], sqrt(3)))
