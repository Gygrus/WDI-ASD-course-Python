"""
Dana jest tablica t[N][N] (reprezentująca szachownicę) wypełniona liczbami całkowitymi z zakresu -9 ..9. Proszę napisać funkcję.która
ustawia na szachownicy dwie wieŹe, tak aby suma liczb na szachowanych polach była największa. Do funkcji należy przekazać tablicę, funkcja
powinna zwrócić położenie wież'
"""
from random import randint


def najwiekszasuma(t):
    result = ''
    for p in range(2):
        sum_of_line = [0] * len(t)
        sum_of_col = [0] * len(t)
        for x in range(len(t)):
            for y in range(len(t)):
                sum_of_line[x] += t[x][y]
                sum_of_col[x] += t[y][x]

        biggest_line = 0
        result_line = 0
        biggest_col = 0
        result_col = 0
        for x in range(len(sum_of_line)):
            if sum_of_line[x] > biggest_line:
                biggest_line = sum_of_line[x]
                result_line = x

            if sum_of_col[x] > biggest_col:
                biggest_col = sum_of_col[x]
                result_col = x

        result += "(" + str(result_line) + str(result_col) + ")"

        for x in range(len(t)):
            t[result_line][x] = 0
            t[x][result_col] = 0


        result += ' '

        for x in range(len(t)):
            print(t[x])
        print()
        print(biggest_line)
        print(biggest_col)
        print()

    return result




t = [0]*10
for x in range(len(t)):
    t[x] = [randint(-9, 9) for _ in range(10)]
    print(t[x])
print()

print(najwiekszasuma(t))

