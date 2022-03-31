x = int(input("> "))
k = x
n = 0
while x != 0:
    x = (x - (x % 10))//10
    n += 1

for i in range(2**n):
    z = 2**n - i - 1
    bin = ""
    while z != 0:
        bin += str(z%2)
        z = z//2

    new = ""
    p = 0
    for t in bin:
        if t == "1":
            new += str(k)[p]
        p += 1
    if new == '':
        pass
    elif int(new) % 7 == 0:
        print(new)
