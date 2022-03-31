def sumowanie(a):
    result = 0
    for x in str(a):
        result += int(x)
    return result

def dzielniki(b):
    n = 2
    result = ""
    while b != 1:
        if b % n == 0:
            result += str(n)
            b  = b // n
        else:
            n += 1
    sum = 0
    for x in result:
        sum += int(x)
    return sum

for x in range(1, 1000000):
    if sumowanie(x) == dzielniki(x):
        print(x)
