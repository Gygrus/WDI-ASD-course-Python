"""
Dana jest tablica int t[N] wypeªniona liczbami caªkowitymi. Prosz¦ napisa¢ funkcj¦, która sprawdza, czy
mo»liwe jest "poci¦cie" tablicy na co najmniej 2 kawaªki o jednakowych sumach elementów. Do funkcji nale»y
przekaza¢ tablic¦, funkcja powinna zwróci¢ najwi¦ksz¡ liczb¦ kawaªków, na któr¡ mo»na poci¡¢ tablic¦, lub
warto±¢ 0, je±li takie poci¦cie nie jest mo»liwe. Na przykªad: dla tablicy [1,2,3,1,5,2,2,2,6] odpowiedzi¡
powinno by¢ 4, bo [1,2,3|1,5|2,2,2|6].
"""
def check_if_prime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def get_all_divisors(n):
    i = 2
    result = []
    while i != n//2 + 1:
        if n%i == 0:
            result.append(i)
        i += 1
    return result


def check_if_possible(T):
    if len(get_all_divisors(sum(T))) == 0:
        return 0
    maximum = 0
    result = []
    def rekur(T, current, cur_tab, i, k, mini_result):
        #print(current, cur_tab, i, k)
        nonlocal maximum, result, check
        cur_tab = cur_tab[:]
        mini_result = mini_result[:]
        if current == k:
            mini_result.append(cur_tab)
            rekur(T, 0, [], i, k, mini_result)
        if current > k:
            return
        if i == len(T) and current == 0:
            check = True
            a = sum(T)//k
            if a > maximum:
                maximum = sum(T)//k
                result = mini_result
                return

        if not check:
            rekur(T, current+T[i], cur_tab + [T[i]], i+1, k, mini_result)

    for k in get_all_divisors(sum(T)):
        check = False
        rekur(T, 0, [], 0, k, [])

    return maximum, result

print(check_if_possible([ 6, 5, 4, 1, 1, 1, 6, 3, 6, 8, 3, 6, 1, 2, 5 ,8]))

