"""
 Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej liczbie muszą
wystąpić wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb
wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375,
17523, 75123, 17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można
zbudować z dwóch zadanych liczb.
"""
from math import sqrt, ceil

def ile_pierwszych(a, b):

    def czy_pierwsza(x):
        for p in range(2, ceil(sqrt(x)) + 1):
            if x % p == 0:
                return False
        return True

    def length_of_num(a):
        count = 0
        while a != 0:
            count += 1
            a //= 10
        return count



    sum_of_all = 0


    binar = length_of_num(a) + length_of_num(b)
    binar = 2**binar
    for x in range(binar):
        combinations = [0]*(length_of_num(a) + length_of_num(b))
        i = 0
        count_of_ones = 0
        while x != 0:
            if x % 2 == 1:
                combinations[i] += x % 2
                count_of_ones += 1
            i += 1
            x //= 2
        if count_of_ones == length_of_num(a):
            print(combinations)
            result = 0
            count_a = length_of_num(a)
            count_b = length_of_num(b)
            for p in combinations:
                result *= 10
                if p == 1:
                    result += (a // 10**((count_a) - 1)) % 10
                    count_a -= 1
                else:
                    result += (b // 10**((count_b) - 1)) % 10
                    count_b -= 1

            print(result)
            if czy_pierwsza(result):
                print(result, "hurraaaaa")
                sum_of_all += 1

    return sum_of_all


print(ile_pierwszych(87843, 7855))

