from math import sqrt

n = int(input())
t = [True]*n
t[0] = t[1] = False
for i in range(2, int(sqrt(n))+1):
    if t[i]:
        for x in range(i**2, n, i):
            t[x] = False

for i in range(n):
    if t[i]:
        print(i)