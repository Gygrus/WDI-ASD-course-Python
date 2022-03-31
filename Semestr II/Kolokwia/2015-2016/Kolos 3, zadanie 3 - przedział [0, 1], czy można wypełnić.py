"""
Zbiór przedziałów {[a1, b1], ..., [an, bn]}, każdy przedział należy do [0, 1]. Opisać algorytm który
sprawdzi czy jest możliwy taki wybór przedziałów, aby cały przedział [0, 1] zawierał się w
wybranych odcinkach. Przedział ma składać się z jak najmniejszej ilości odcinków.
"""


"""
Algorytm zachłanny: sortujemy przedziały po pierwszej współrzędnej (O(nlogn)). Następnie sprawdzamy czy początek pierwszego
przedziału jest w 0, jeśli nie to kończymy algorytm, jeśli tak, to zapamiętujemy koniec rozważanego przedziału i sprawdzamy
kolejne przedziały. Z tych przedziałów, które pierwszą współrzędną mają mniejszą (lub równą) niż druga współrzędna zapamiętanego przedziału,
zapamiętujemy ten, który ma drugą współrzędną największą, następnie zapamiętujemy tą współrzędną. Proces powtarzamy, jeśli 
podczas przeszukiwania nie natrafimy na żaden przedział, to znaczy że przedział nie może zostać wypełniony (istnieje przerwa
między przedziałami), a jeśli największa druga współrzędna z przedziałów jest mniejsza niż ta, do której porównywamy, również
oznacza, że nie da się wypełnić [0, 1] tymi przedziałami. Ostatnia zapamiętana druga współrzędna powinna być równa 1 żeby zwrócić
prawdę.
Analiza złożoności: sortowanie nlogn, przejście i wybór przedziałów liniowe (n).
"""
from random import uniform

def filling_a_span(list):
    n = len(list)

    def quicksort1(Tab, p, r):
        def quicksort(Tab, p, r):
            while p < r:
                q = partition(Tab, p, r)
                quicksort(Tab, p, q - 1)
                p = q + 1

        def partition(Tab, p, r):
            x = Tab[r][0]
            i = p - 1
            for j in range(p, r):
                if Tab[j][0] < x:
                    i += 1
                    Tab[i], Tab[j] = Tab[j], Tab[i]
            Tab[i + 1], Tab[r] = Tab[r], Tab[i + 1]
            return i + 1

        quicksort(Tab, p, r)

    quicksort1(list, 0, n-1)
    print(list)
    if list[0][0] != 0:
        return False

    if list[0][1] == 1:
        return True

    max = 0
    current = list[0][1]
    counter = 1
    result = [list[0]]
    rem = []
    for x in range(1, n):
        # print(result, max, current, list[x])
        print(result)
        if list[x][0] <= current:
            if list[x][1] > max:
                max = list[x][1]
                rem = list[x]
        elif list[x][0] > current:
            if max == 0:
                return False
            else:
                current = max
                result.append(rem)

                if current == 1:
                    return True, counter + 1, result

                max = 0
                if list[x][0] <= current:
                    max = list[x][1]
                    rem = list[x]
                    counter += 1

                counter += 1

    if max == 1:
        result.append(rem)
        return True, counter, result

    return False


list = [[0.2, 0.4], [0.1, 0.3], [0.5, 0.8], [0.6, 0.7], [0.9, 1], [0.6, 0.8], [0, 0.6], [0.7, 1]]
a = uniform(0, 1)
b = uniform(0, 1)
c = uniform(0, 1)
d = uniform(0, 1)
e = uniform(0, 1)
f = uniform(0, 1)
g = uniform(0, 1)
h = uniform(0, 1)
a1 = uniform(a, 1)
b1 = uniform(b, 1)
c1 = uniform(c, 1)
d1 = uniform(d, 1)
e1 = uniform(e, 1)
f1 = uniform(f, 1)
g1 = uniform(g, 1)
h1 = uniform(h, 1)
start = uniform(0.1, 1)
stop = uniform(0.6, 1)
list1 = [[a, a1], [b, b1], [c, c1], [d, d1], [stop, 1], [e, e1], [0, start], [f, f1], [g, g1], [h, h1]]
print(filling_a_span(list1))
