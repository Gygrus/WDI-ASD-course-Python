from random import randint


def biggest_subset(T):

    def get_length(elem):
        return elem[1]-elem[0]

    def sort_sets(T):
        new = list()
        for x in T:
            new.append((x, get_length(x)))
        return mergesort(new)


    def mergesort(T):
        def merge(t1, t2):
            n, m = len(t1), len(t2)
            i = j = 0
            result = list()
            while i < n and j < m:
                if t1[i][1] > t2[j][1]:
                    result.append(t1[i])
                    i += 1
                else:
                    result.append(t2[j])
                    j += 1
            if i >= n and j < m:
                result = result + t2[j:m]
            elif i < n and j >= m:
                result = result + t1[i:n]

            return result

        def rekur(T, a, b):
            n = b - a + 1
            m = a + (b - a) // 2
            if n == 2:
                if T[a][1] > T[b][1]:
                    return [T[a], T[b]]
                else:
                    return [T[b], T[a]]
            if n == 1:
                return [T[a]]

            result1 = rekur(T, a, m)
            result2 = rekur(T, m + 1, b)

            return merge(result1, result2)

        return rekur(T, 0, len(T) - 1)

    new = sort_sets(T)
    print(new)
    biggest = 0
    result = None
    for x in range(0, len(new)-1):
        if biggest >= len(new)-x-1:
            return result, biggest

        current = 0
        for y in range(x+1, len(new)):
            if new[x][0][0] <= new[y][0][0] and new[x][0][1] >= new[y][0][1]:
                current += 1

        if current > biggest:
            biggest = current
            result = new[x][0]

    return result, biggest


#p = sort_sets(T)
T = [(randint(-1000, 1000), randint(-1000, 1000)) for _ in range(40000)]
#T = [(1, 5), (2, 6), (0, 4), (8, 24), (3, 13), (-5, 7)]
print(T)
print(biggest_subset(T))