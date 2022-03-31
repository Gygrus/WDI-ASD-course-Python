x = int(input("> "))
n = x
count = 0
while n > 0:
    n = n // 10
    count += 1
j = 0
k = True
while x > 0:
    j = x % 10
    if j == count:
        print("gówno")
        k = False
        break
    x = x // 10
if k:
    print("dupa")


# for i in str(x):
#     if int(i) == len(str(x)):
#         print(True)
