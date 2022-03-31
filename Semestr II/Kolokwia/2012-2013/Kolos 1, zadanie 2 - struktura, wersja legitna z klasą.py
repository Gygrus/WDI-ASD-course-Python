"""
Proszę zaprojektowac strukturę danych przechowującą liczby i pozwalającą na następujące
operacje (zakładamy, że wszystkie liczby umieszczane w strukturze są różne):
Init(n). Tworzy zadaną strukturę danych zdolną pomieścić maksymalnie n liczb.
Insert(x). Dodaje do struktury liczbę x.
RemoveMin() Znajduje najmniejszą liczbę w strukturze, usuwa ją i zwraca jej wartość.
RemoveMax() Znajduje największą liczbę w strukturze, usuwa ją i zwraca jej wartość.
Każda z operacji powinna mieć złożoność O(log n, gdzie n to ilość liczb znajdujących się obecnie
w strukturze. W tym zadaniu nie trzeba implementować podanych operacji, a jedynie
przekonująco opisać jak powinny być zrealizowane i dlaczego mają wymaganą złożoność.
"""


class Structure_2:
    def __init__(self, T):
        self.length = 0
        self.minheap = [T[i] for i in range(len(T))]
        self.maxheap = [T[i] for i in range(len(T))]
        self.index_from_min_to_max = [T[i] for i in range(len(T))]
        self.index_from_max_to_min = [T[i] for i in range(len(T))]

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def minHeapify(self, minheap, maxheap, length, i):
        l = self.left(i)
        r = self.right(i)
        m = i
        print(m, l, r)

        if l < length and self.minheap[l] < self.minheap[m]:
            m = l

        if r < length and self.minheap[r] < self.minheap[m]:
            m = r

        if m != i:
            self.minheap[i], self.minheap[m] = self.minheap[m], self.minheap[i]
            self.index_from_max_to_min[self.index_from_min_to_max[i]], self.index_from_max_to_min[self.index_from_min_to_max[m]] = self.index_from_max_to_min[self.index_from_min_to_max[m]], self.index_from_max_to_min[self.index_from_min_to_max[i]]
            self.minHeapify(minheap, maxheap, length, m)


    def maxHeapify(self, minheap, maxheap, length, i):
        l = self.left(i)
        r = self.right(i)
        m = i

        if l < length and self.maxheap[l] > self.maxheap[m]:
            m = l

        if r < length and self.maxheap[r] > self.maxheap[m]:
            m = r

        if m != i:
            self.maxheap[i], self.maxheap[m] = self.maxheap[m], self.maxheap[i]
            self.index_from_min_to_max[self.index_from_max_to_min[i]], self.index_from_min_to_max[
                self.index_from_max_to_min[m]] = self.index_from_min_to_max[self.index_from_max_to_min[m]], \
                                                 self.index_from_min_to_max[self.index_from_max_to_min[i]]

            self.maxHeapify(minheap, maxheap, length, m)




    def Init(self, n):
        self.lenth = n
        for x in range(self.parent(n-1), -1, -1):
            self.minHeapify(self.minheap, self.maxheap, self.length, x)
            self.maxHeapify(self.minheap, self.maxheap, self.length, x)

    def Princior(self):
        print(self.minheap)
        print(self.maxheap)


T = [3, 2, 7, 54, 32, 62, 1, 2, 8, 9]
T = Structure_2(T)
T.Init(10)
T.Princior()


