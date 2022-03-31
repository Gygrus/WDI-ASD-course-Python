"""
Punkt leżący na płaszczyźnie jest opisywany parą liczb typu float (x,y). Tablica T[N] zawiera
współrzędne N punktów leżących na płaszczyźnie. Punkty posiadają jednostkową masę. Proszę napisać funkcję,
która sprawdza czy istnieje niepusty podzbiór n punktów, gdzie n¡k oraz n jest wielokrotnością liczby
3, którego środek ciężkości leży w odległości mniejszej niż r od początku układu współrzędnych. Do funkcji
należy przekazać dokładnie 3 parametry: tablicę t, promień r, oraz ograniczenie k, funkcja powinna zwrócić
wartość typu bool.
"""
from math import sqrt

def rekur(T, r, k):

    def count_distance(set_of_numbers):
        av_x = 0
        av_y = 0
        for x in set_of_numbers:
            av_x += x[0]
            av_y += x[1]
        av_x /= len(set_of_numbers)
        av_y /= len(set_of_numbers)
        return sqrt(av_x**2 + av_y**2)

    def check_if_exists(T, set_of_points, i, r, k):
        print(set_of_points)
        if i == len(T):
            if len(set_of_points) % 3 == 0 and len(set_of_points) <= k and len(set_of_points) > 0:
                if count_distance(set_of_points) < r:
                    print(count_distance(set_of_points))
                    return True
                else:
                    return False

        else:
            new_set = list(set_of_points)
            new_set.append(T[i])
            new_set = tuple(new_set)
            return check_if_exists(T, set_of_points, i+1, r, k) or check_if_exists(T, new_set, i+1, r, k)

    if check_if_exists(T, tuple(), 0, r, k):
        return True
    else:
        return False


print(rekur([[234, 5], [4, 1], [0, 5], [0, 9], [4362, 5], [0, 1]], 5.02, 3))



