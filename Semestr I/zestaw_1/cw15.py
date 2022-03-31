import math
def cw15():
    e = 10**-12
    previous = 0
    result = 1
    c = 123123
    while abs(result - c) > e:
        c = result
        k = math.sqrt(1/2 + previous*(1/2))
        result *= k
        previous = k

    print(result)
    print(2/result)

cw15()