"""
f(0,b) = b+1
f(a,0) = f(a-1,1)           a > 0
f(a,b) = f(a-1, f(a, b-1))  a > 0, b > 0
"""
def f(a, b):
    def func(a, b):
        if a == 0:
            return b+1
        elif b == 0:
            return func(a-1, 1)
        else:
            return func(a-1, func(a, b-1))
    #func(a, b)

    return func(a, b)

print(f(4, 1))