from math import factorial

def cw17(a, b):
    result = 4
    compare = 3
    e = 10**-8
    while abs(result - compare) > e:
        compare = result
        c = a + b
        b = a
        a = c
        result = a/b
    print(result)

cw17(1, 1)

def cw19():
    compare = 34526
    e = 10**-8
    sum = 0
    x = 0
    while abs(sum - compare) > e:
        compare = sum
        result = 1/factorial(x)
        sum += result
        x += 1
    print(sum)

cw19()