count = 0


def rekur(n, string, i):
    if i == n:
        global count
        count += 1
        print(string[1:])
        return
    if string[-1] == "1":
        for x in range(1, 6):
            rekur(n, string+str(x), i+1)
    else:
        for x in range(1, 3):
            rekur(n, string+str(x), i+1)

n = 5

for x in range(1, 3):
    rekur(n, '0'+str(x), 1)

print(count)