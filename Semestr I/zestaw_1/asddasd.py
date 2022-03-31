x = int(input())


a = 1
b = 1
c = 0

while c < x:
    if a*b == x:
        print("Tak, jest iloczynem apodsjapdj")
        print("a =", a, "b = ", b)
    c = a + b
    a = b
    b = c


