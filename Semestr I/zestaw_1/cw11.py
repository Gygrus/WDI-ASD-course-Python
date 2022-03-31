k = 0
for x in range(1, 10000001):
    sum = 0
    for i in range(1, x//2 + 1):
        if x % i == 0:
            sum += i

    second = 0
    for i in range(1, sum//2 + 1):
        if sum % i == 0:
            second += i
    if second == x and x != sum:
        if k % 2 == 0:
            print(x, sum)
        k += 1