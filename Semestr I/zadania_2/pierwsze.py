from math import sqrt
print(2, 3)
n = 1
while n <= 100000:
    result = 0
    for x in str(n):
        result += int(x)**len(str(n))
    if result == n:
        print(n)
    n += 1