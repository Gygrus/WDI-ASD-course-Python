from math import sqrt

x = int(input())

dif = x + 1
i = 1
while i < sqrt(x):
    if x % i == 0 and abs(x/i - i) < dif:
        dif = int(abs(x/i - i))
        result = (int(i), int(x/i))
    i += 1

print(result, dif)


