def cw14(x):
    e = 10**-12
    previous = 55
    sum = 0
    a = 0
    minus = False
    while abs(sum - previous) > e:
        previous = sum
        factorial = 1
        for i in range(1, a + 1):
            factorial *= i
        if minus:
            sum -= (x**a)/factorial
            minus = False
        else:
            sum += (x**a)/factorial
            minus = True
        a += 2

    print(sum)


cw14(241)
