"""
Dane są dwie tablice t1[N] i t2[N] zawierające liczby naturalne. Z wartości w obu tablicach
możemy tworzyć sumy. „Poprawna” suma to taka, która zawiera co najmniej jeden element
(z tablicy t1 lub t2) o każdym indeksie. Na przykład dla tablic: t1 = [1,3,2,4] i t2 = [9,7,4,8]
poprawnymi sumami są na przykład 1+3+2+4, 9+7+4+8, 1+7+3+8, 1+9+7+2+4+8.
Proszę napisać funkcję generującą i wypisującą wszystkie poprawne sumy, które są liczbami
pierwszymi. Do funkcji należy przekazać dwie tablice, funkcja powinna zwrócić liczbę
znalezionych i wypisanych sum.
"""
from random import randint
from math import sqrt, ceil

def f(t1, t2):
    komb = 2**len(t1)
    count = 0
    for x in range(komb):
        check = ''
        while x != 0:
            check += str(x%2)
            x //= 2

        while len(check) != len(t1):
            check += '0'

        temp_1 = t1
        temp_2 = t2
        result = 0

        for x in range(len(check)):
            if check[x] == "1":
                result += temp_1[x]
                temp_1[x] = 0
            else:
                result += temp_2[x]
                temp_2[x] = 0

        new_t1 = ''
        for i in temp_1:
            if i != 0:
                new_t1 += str(i)

        komb_1 = 2 ** len(new_t1)
        for y in range(komb_1):
            check_1 = ''
            while y != 0:
                check_1 += str(y%2)
                y //= 2

            while len(check_1) != len(new_t1):
                check_1 += '0'

            for k in range(len(check_1)):
                if check_1[k] == 1:
                    result += new_t1[k]

            new_t2 = ''
            for i in temp_2:
                if i != 0:
                    new_t2 += str(i)

            komb_2 = 2 ** len(new_t2)
            for z in range(komb_2):
                check_2 = ''
                while z != 0:
                    check_2 += str(z % 2)
                    z //= 2

                while len(check_2) != len(new_t2):
                    check_2 += '0'

                for k in range(len(check_2)):
                    if check_1[k] == 1:
                        result += new_t2[k]

                if_true = True
                for p in range(2, ceil(sqrt(result)) + 1):
                    if result % p == 0:
                        if_true = False
                        break

                if if_true:
                    count += 1
                    print(result, new_t1, new_t2)

    return count



t_1 = [randint(1,9) for _ in range(5)]
t_2 = [randint(1,9) for _ in range(5)]
print(t_1)
print(t_2)
print(f(t_1, t_2))