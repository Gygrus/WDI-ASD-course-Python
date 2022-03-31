from math import sqrt

x = int(input())

a = 1
b = 1
z = False
while a <= x:
    c = a + b
    b = a
    a = c
    a_1 = 1
    b_1 = 1
    print(a, b)
    while a_1 <= a:
        c_1 = a_1 + b_1
        b_1 = a_1
        a_1 = c_1
        if b * a_1 == x or b * b_1 == x:
            z = True
            break
print(z)