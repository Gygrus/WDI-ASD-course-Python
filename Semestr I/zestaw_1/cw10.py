def cw10():
    for x in range(2, 1000000):
        sum = 0

        z = x // 2
        for k in range(1, z + 1):
            if x % k == 0:
                sum += k
        if sum == x:
            print(x)


cw10()