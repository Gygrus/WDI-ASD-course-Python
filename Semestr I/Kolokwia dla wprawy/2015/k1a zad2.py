"""
Proszę napisać program, który wypełnia tablicę t[N] pseudolosowymi liczbami nieparzystymi z zakresu [1..99],
a następnie Wyznacza i wypisuje różnicę pomiędzy długością najdłuższego znajdującego się w niej ciągu
arytmetycznego o dodatniej różnicy, a długością najdłuższego ciągu arytmetycznego o ujemnej różnicy, przy
założeniu, że kolejnymi wyrazami ciągu są elementy tablicy o kolejnych indeksach.
"""
from random import randint

def difference(t):
    z_end_plus = True
    z_end_minus = True
    b = len(t) - 1
    while b > 0:
        if not z_end_plus and not z_end_minus:
            break

        for x in range(len(t) - b):
            r = t[x+1] - t[x]
            if r > 0:
                z_plus = True
                z_minus = False

            elif r < 0:
                z_minus = True
                z_plus = False

            else:
                z_plus = False
                z_minus = False

            for y in range(x, b + x):
                if z_plus and z_end_plus:
                    if t[y + 1] - t[y] != r:
                        z_plus = False
                        break

                elif z_end_minus and z_minus:
                    if t[y + 1] - t[y] != r:
                        z_minus = False
                        break

            if z_plus and z_end_plus:
                result_plus = b + 1
                z_end_plus = False

            if z_minus and z_end_minus:
                result_minus = b + 1
                z_end_minus = False

        b -= 1

    return result_plus - result_minus, result_plus, result_minus
    # a = 0
    # b = len(t) - 1
    # count_plus = 1
    # count_minus = 1
    # while a <= b:
    #     count_temp_pl = 1
    #     count_temp_ms = 1
    #     r = t[a + 1] - t[a]
    #     for x in range(a, b):
    #         if
    #         new_r = t[x + 1] - t[x]
    #         if new_r != r:
    #             if count_temp_pl > count_plus:
    #                 count_plus = count_temp_pl
    #
    #             if count_temp_ms > count_minus:
    #                 count_minus = count_temp_ms
    #
    #             if new_r < 0:
    #                 count_temp_ms = 2
    #                 count_temp_pl = 1
    #
    #             if new_r > 0:
    #                 count_temp_ms = 1
    #                 count_temp_pl = 2
    #
    #             r = new_r
    #
    #         else:
    #             if r > 0:
    #                 count_temp_pl += 1
    #             elif r < 0:
    #                 count_temp_ms += 1
    #
    #     a += 1
    #     b -= 1
    #
    # return count_plus - count_minus, count_plus, count_minus




#t = [randint(1, 10) for _ in range(10)]
t = [5, 6, 5, 4, 5, 3, 2, 1, 3, 2, 4, 62, 7, -9, -3, 3, 9, 15, 21, 27, 76, 74, 72, 70, 68]
print(t)
print(difference(t))