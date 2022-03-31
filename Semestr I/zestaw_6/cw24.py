"""
Tablica T = [(x1, y1),(x1, y1), ...] zawiera położenia N punktów o współrzędnych opisanych
wartościami typu float. Proszę napisać funkcję, która zwróci najmniejszą odległość między środkami ciężkości
2 niepustych podzbiorów tego zbioru
"""
from random import randint
from math import sqrt

def get_lowest_distance(tab):
    lowest = 10**100
    for x in range(len(tab)-1):
        for y in range(x+1, len(tab)):
            #print(tab[x], tab[y])
            if sqrt((tab[x][0] - tab[y][0])**2 + (tab[x][1] - tab[y][1])**2) < lowest:
                lowest = sqrt((tab[x][0] - tab[y][0])**2 + (tab[x][1] - tab[y][1])**2)
                #print(lowest)
                #print(tab[x], tab[y])

    if lowest == 10**100:
        return False

    return lowest



def rekur(T):
    tab_of_centres = list()
    set_of_points = tuple()
    def get_centres(T, i, count, set_of_points):
        if i == len(T):
            if count >= 1:
                x_of_point = 0
                y_of_point = 0
                for x in set_of_points:
                    x_of_point += x[0]
                    y_of_point += x[1]
                x_of_point /= count
                y_of_point /= count
                tab_of_centres.append((x_of_point, y_of_point))
        else:
            get_centres(T, i+1, count, set_of_points)
            set_of_points = list(set_of_points)
            set_of_points.append(T[i])
            set_of_points = tuple(set_of_points)
            get_centres(T, i+1, count+1, set_of_points)

    get_centres(T, 0, 0, set_of_points)

    print(tab_of_centres)
    return get_lowest_distance(tab_of_centres)



T = [[randint(-50,50) for _ in range(2)] for _ in range(10)]

print(T)

print(rekur(T))

