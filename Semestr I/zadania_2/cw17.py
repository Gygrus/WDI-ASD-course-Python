ep = 1e-8
x = 5
k = x
compare = 0
k = 0
while abs(x - compare) > ep:
    compare = x
    a = x**x - 27
    b = x**x
    x = x - (a/b)
    print(x)
    k += 1
print(x)