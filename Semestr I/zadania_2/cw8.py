def cw8(a, b, n):
    x = a//b
    y = a%b
    k = str(x) + '.'
    while n > 0:
        y *= 10
        k += str(y//b)
        y = y - (y//b * b)
        n -= 1
    print(k)

cw8(2, 57, 999)