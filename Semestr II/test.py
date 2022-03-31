a = 1
b = 1
n = 45662
c = a+b
for x in range(0, n-3):
    b = a
    a = c
    c = a+b

print(c)