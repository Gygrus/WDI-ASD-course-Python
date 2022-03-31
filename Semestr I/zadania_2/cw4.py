n = int(input())

a = 0

count = 0
while 2**a <= n:
    b = 0
    while 3**b <= n:
        c = 0
        while 5**c <= n:
            if 2**a * 3**b * 5**c <= n:
                count += 1
                print(a, b, c)
                print(2**a * 3**b * 5**c)
            c += 1
        b += 1
    a += 1

print(count)

