def is_prime(n):
    if n < 2:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
#end

def get_num_length_rec(n):
    if n == 0:
        return 0
    return 1 + get_num_length_rec(n // 10)


def get_num_length(n):
    dc = 0
    while n > 0:
        dc += 1
        n //= 10

    return dc
    #'''
    #return ceil(log10(n))
    #'''
#end

def delete_digit(n, i):
    tail = n % (10**(i-1))
    head = (n - (n % (10**(i-1)))) // 10
    return head + tail
    #
    #return int(str(n)[:i] + str(n)[i:])



def rec(num, last_i, cl, ol):
    if cl < ol:
        if is_prime(num):
            print(num)

    for i in range(last_i, cl + 1):
        cn = delete_digit(num, i)
        rec(cn, i, cl - 1, ol)



def f(num):
    l = get_num_length(num)
    rec(num, 1, l, l)

f(123)
