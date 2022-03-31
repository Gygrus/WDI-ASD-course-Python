from math import sqrt

def cw20(a, b):
    e = 10**-12
    a_n = 0
    b_n = 0
    result = 0
    previous_a = 24
    previous_b = 24

    while abs(a - previous_a) > e and abs(b - previous_b) > e:
        previous_a = a
        previous_b = b
        a_n = sqrt(a*b)
        b_n = (a+b)/2.0
        a = a_n
        b = b_n
    print(a, b)

cw20(5, 34)