from math import sqrt

x = int(input())

a = 2

while a <= x:
    if x % a == 0:
        print("Tak")
        break
    a = 3*a + 1
