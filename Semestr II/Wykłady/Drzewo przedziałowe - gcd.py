from math import gcd
def build_tree(arr, n):
    tree = [1] * (2 * (n))
    for i in range(n):
        tree[i + n] = arr[i]

    for i in range(n - 1, 0, -1):
        tree[i] = gcd(tree[2 * i], tree[2 * i + 1])

def get_ans(a, b, tree, n):
    res = 0
    a += n
    b += n
    while a < b:
        if a & 1:
            res = gcd(tree[a], res)
            a += 1
        if b & 1:
            b -= 1
            res = gcd(tree[b], res)

        a >>= 1
        b >>= 1
    return res