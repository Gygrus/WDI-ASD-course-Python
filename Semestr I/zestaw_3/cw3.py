from math import sqrt
n = int(input(">"))

x = list(range(2, n))

# k = 2
# new = []
# while k <= sqrt(n):
#     i = 0
#     z = set()
#     if k in x:
#         new.append(k)
#         z = set(range(k, len(x) + 2, k))
#         x = list(set(x) - set(z))
#     k += 1
# print(x)


k = 2
new = []
while k <= sqrt(n):
    if k in x:
        new.append(k)
        i = 0
        while i < len(x):
            if x[i] % k == 0:
                del x[i]

            else:
                i += 1
    k += 1



print(new + x)


