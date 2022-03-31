from math import inf
"""
Szukamy najmniejszej liczby tankowań na dotarcie do celu oddalonego od t.
"""


def tank_refuel_a(S, L, t):
    n = len(S)
    counter = 0
    curr_pos = 0
    curr_idx = -1
    while (t - curr_pos) > L:
        prev = 0
        check = False
        curr_idx += 1
        while curr_idx < n and (S[curr_idx] - curr_pos) <= L:
            check = True
            prev = curr_idx
            curr_idx += 1


        if check:
            curr_pos = S[prev]
            curr_idx -= 1
            counter += 1
        else:
            print("Nie da się przemieścić do t!")
            return

    return counter

# S = [200, 375, 700, 900]
# L = 400
# t = 1150
# print(tank_refuel_a(S, L, t))

"""
b) tablica P[i] przechowuje ceny paliwa za litr.
Szukamy drogi o minimalnym koszcie
Przemieszczamy się z miasta i do pierwszego miasta o niższej cenie paliwa niż cena P[i] (jeśli istnieje). 
Kupujemy wtedy tylko tyle paliwa aby dojechać do P[i].
Jeśli najmniejszy koszt z przedziału S[i], S[i]+L jest większy niż P[i]
to kupujemy paliwo z P[i] do pełnego baku, przemieszczając się potem do stacji
z najmniejszą ceną.
"""


def tank_refuel_b1(S, P, L, t):
    n = len(S)
    curr_fuel = L
    prev_index = 0
    curr_pos = 0
    curr_price = 0
    curr_idx = 0
    total_cost = 0
    chosen_city = 0
    while (t-curr_pos) > L:
        print(curr_pos, total_cost, curr_fuel)
        min_cost = inf
        curr_idx = chosen_city+1
        while curr_idx < n and (S[curr_idx] - curr_pos) <= L:
            print(P[curr_idx], min_cost)
            if P[curr_idx] < min_cost:
                chosen_city = curr_idx
                min_cost = P[curr_idx]
                if min_cost < curr_price:
                    curr_idx += 1
                    break

            curr_idx += 1


        if min_cost < curr_price:
            if (S[chosen_city] - S[prev_index] - curr_fuel) > 0:
                total_cost += (S[chosen_city] - S[prev_index] - curr_fuel)*curr_price
                pom = curr_fuel
                curr_fuel += S[chosen_city] - S[prev_index] - pom

        else:
            total_cost += (L-curr_fuel)*curr_price
            curr_fuel += (L-curr_fuel)

        print(chosen_city)
        curr_idx -= 1
        curr_fuel -= (S[chosen_city] - S[prev_index])
        curr_pos = S[chosen_city]
        prev_index = chosen_city
        curr_price = min_cost


    print(curr_pos, total_cost, curr_fuel)
    if (t - curr_pos) <= curr_fuel:
        return total_cost
    else:
        while (t-curr_pos) > curr_fuel:
            print(curr_pos, total_cost, curr_fuel)
            min_cost = inf
            curr_idx = chosen_city + 1
            while curr_idx < n and (S[curr_idx] - curr_pos) <= L:
                print(P[curr_idx], min_cost)
                if P[curr_idx] < min_cost:
                    chosen_city = curr_idx
                    min_cost = P[curr_idx]
                    if min_cost < curr_price:
                        curr_idx += 1
                        break

                curr_idx += 1

            if min_cost < curr_price:
                if (S[chosen_city] - S[prev_index] - curr_fuel) > 0:
                    total_cost += (S[chosen_city] - S[prev_index] - curr_fuel) * curr_price
                    pom = curr_fuel
                    curr_fuel += S[chosen_city] - S[prev_index] - pom

            else:
                total_cost += ((t-curr_pos) - curr_fuel) * curr_price
                curr_fuel += ((t-curr_pos) - curr_fuel)
                break

            print(chosen_city)
            curr_idx -= 1
            curr_fuel -= (S[chosen_city] - S[prev_index])
            curr_pos = S[chosen_city]
            prev_index = chosen_city
            curr_price = min_cost

    return total_cost


# S = [0, 30, 45, 70, 95, 103, 120, 160, 162, 190, 240]
# P = [0, 4, 2, 1, 0.6, 3, 4, 1, 1.6, 3.4, 2]
# L = 60
# t = 250

# print(tank_refuel_b1(S, P, L, t))



def tank_refuel_b1_dynamic(S, P, L, t):
    n = len(S)
    F = [0 for _ in range(t+1)]
    first_station = 1
    last_station = 0
    for x in range(n):
        if S[x] <= L:
            last_station = x
        else:
            break
    for x in range(L+1, t+1):
        min = inf
        for y in range(first_station, last_station+1):
            if P[y] < min:
                min = P[y]

        if S[first_station] <= x - L:
            first_station += 1

        if last_station != n-1 and x == S[last_station+1]:
            last_station += 1

        F[x] += F[x-1] + min


    return F[t]


# S = [0, 30, 45, 70, 95, 103, 120, 160, 162, 190, 200, 240]
# P = [0, 4, 0.4, 1, 0.6, 3, 4, 1, 1.6, 3.4, 0.7, 2]
# L = 60
# t = 250
L = 10
S = [0, 8, 11, 15, 16]
P = [0, 40, 7, 15, 12]
t = 23
#
print(tank_refuel_b1(S, P, L, t))
# print("dupa")
L = 10
S = [0, 8, 11, 15, 16]
P = [0, 40, 7, 15, 12]
t = 23
print(tank_refuel_b1_dynamic(S, P, L, t))


def tank_refuel_b2_dynamic_improved(S, P, L, t):
    S.append(t)
    P.append(0)
    n = len(S)
    F = [ [0 for _ in range(2)] for _ in range(n)]

    first_station = 1
    last_station = 0
    for x in range(1, n):
        if S[x] <= L:
            F[x][1] = L-S[x]
        else:
            last_station = x-1
            break

    for x in range(1, last_station):
        if S[last_station+1] - S[x] <= L:
            first_station = x
            break

    curr_fuel = -1
    for x in range(last_station + 1, n):
        if S[x] - S[x-1] <= curr_fuel:
            curr_fuel -= S[x] - S[x-1]
            F[x][0] = F[x-1][0]
            F[x][1] = curr_fuel

        else:
            min = inf
            for y in range(first_station, last_station+1):
                # print("station: ", y, S[y])
                # print("(L-F[S[y]][1])*P[y]: ", (L-F[y][1])*P[y])
                # print("F[S[y]][0]: ", F[y][0])
                if ((L-F[y][1])*P[y]) + F[y][0] < min:
                    rem_0 = ((L-F[y][1])*P[y]) + F[y][0]
                    rem_1 =  L-(S[x] - S[y])
                    min = ((L-F[y][1])*P[y]) + F[y][0]

            F[x][0] = rem_0
            F[x][1] = rem_1
            curr_fuel = rem_1

        while x <= n - 2 and S[first_station] <= S[x+1] - L:
            first_station += 1

        last_station += 1

    return F[n-1]

def tank_refuel_b2_dynamic(S, P, L, t):
    n = len(S)
    F = [ [0 for _ in range(2)] for _ in range(t+1)]

    for x in range(1, L+1):
        F[x][1] = L-x
    first_station = 1
    last_station = 0
    for x in range(n):
        if S[x] <= L:
            last_station = x
        else:
            break

    curr_fuel = -1
    for x in range(L+1, t+1):
        if curr_fuel >= 0:
            F[x][0] = F[x-1][0]
            F[x][1] = curr_fuel
            curr_fuel -= 1

        else:
            min = inf
            for y in range(first_station, last_station+1):
                if ((L-F[S[y]][1])*P[y]) + F[S[y]][0] < min:
                    rem_0 = ((L-F[S[y]][1])*P[y]) + F[S[y]][0]
                    rem_1 =  L-(x - S[y])
                    min = ((L-F[S[y]][1])*P[y]) + F[S[y]][0]

            F[x][0] = rem_0
            F[x][1] = rem_1
            curr_fuel = rem_1-1

        if S[first_station] <= x - L:
            first_station += 1

        if last_station != n - 1 and x == S[last_station + 1]:
            last_station += 1

    for x in range(int(len(F)//10)):
        print(x*10, F[x*10+1: x*10 + 11])


    return F[t]

# S = [0, 30, 45, 70, 95, 103, 120, 143, 160, 162, 190, 200, 240]
# P = [0, 4, 0.4, 1, 0.6, 3, 4, 2.7, 1, 1.6, 3.4, 0.7, 2]
# L = 60
# t = 250
# L = 10
# S = [0, 8, 11, 15, 16]
# P = [0, 40, 7, 15, 12]
# t = 23
# # print(tank_refuel_b2_dynamic(S, P, L, t))
# print(tank_refuel_b2_dynamic_improved(S, P, L, t))
# # S = [0, 30, 45, 70, 95, 103, 120, 143, 160, 162, 190, 200, 240]
# # P = [0, 4, 0.4, 1, 0.6, 3, 4, 2.7, 1, 1.6, 3.4, 0.7, 2]
# # L = 60
# # t = 250
# L = 10
# S = [0, 8, 11, 15, 16]
# P = [0, 40, 7, 15, 12]
# t = 23
# print(tank_refuel_b2_dynamic(S, P, L, t))
# # print(tank_refuel_b2_dynamic_improved(S, P, L, t))

