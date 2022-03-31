def cw16():
    result = 0
    for x in range(2, 10001):
        i = x
        sum = 0
        next = 0
        while next != 1:
            next = (x % 2) * (3 * x + 1) + (1 - x % 2) * x / 2
            x = next
            sum += 1
        if sum > result:
            result = sum
            digit = i
    print(result, digit)


cw16()