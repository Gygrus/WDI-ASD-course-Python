n = int(input())

i = 1
f_n = 1
while i <= n:
    if n > 100:
        f_n *= 4
        n -= 100
    if n > 10:
        f_n *= 8
        n -= 10
    else:
        f_n *= n
        n -= 1
while f_n%10 == 0:
    f_n = f_n // 10
print(int(f_n % 10))
if f_n % 10 == 0:
    pass

k = 0
z = 0
while n % 5 == 0:
    n = n/5
    k += 1
while z < k:
    n = n/2
    z += 1