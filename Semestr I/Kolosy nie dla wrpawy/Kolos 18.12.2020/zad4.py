# Piotr Socała

#W kolejnych wywołaniach rekurencyjnych albo tworzę nowy podział, albo dodaję
#cyfrę do poprzedniego i następnie sprawdzam warunki
#
#
#


def check_if_prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1

    return True
#end

def get_length(n):
    copy = n
    counter = 0
    while copy != 0:
        counter += 1
        copy //= 10

    return counter
#end

def get_first_num(n):
    z = get_length(n)
    p = n
    return p // 10**(z-1)


def divide(N):
    how_many_primes = 0
    for x in range(get_length(N)):
        if x > 1 and check_if_prime(x):
            how_many_primes += 1

    result = False
    def rekur(n, new, remaining, next_div, i):
        print(new, remaining, next_div)
        nonlocal result
        if i == 0:
            if check_if_prime(next_div) and check_if_prime(new):
                result = True

            return

        if not result:
            rekur(n, new*10 + get_first_num(remaining), remaining//10**(get_length(remaining)-1), next_div, i-1)
            if not result and check_if_prime(new):
                rekur(n, get_first_num(remaining), remaining//10**(get_length(remaining)-1), next_div+1, i - 1)


    #end
    rekur(N, 0, N, 1, get_length(N))
    return result
#end



