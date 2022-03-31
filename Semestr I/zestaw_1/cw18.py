def cw18(a):
    x = a
    e = 10**-12
    previous = 123
    while abs(x - previous) > e:
        previous = x
        x = ( 2*x + a/x**2 )/3

    print(x)


cw18(16)