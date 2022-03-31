x = int(input())

n = 1

while n <= x:
    if not(x % (n*n+n+1)):
        print("Jest")
        break
    n += 1
