from random import randint, seed
from time import time
seed(42)

class Node:
    def __init__(self):
        self.next = None
        self.value = None


def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        C = X
    return H.next


def printlist(L):
    while L != None:
        print(L.value, "->", end=" ")
        L = L.next
    print("|")


from random import randint, seed
from time import time


class Node:
    def __init__(self):
        self.next = None
        self.value = None


def qsort(L):
    def quicksort(left, right):
        if left.next == right or left == right or right.value is None:
            return

        a, pivot_start_prev, pivot_end, b = partition(left, right)
        if left is not right:
            if pivot_start_prev is not None and a.next != pivot_start_prev:
                quicksort(a, pivot_start_prev)               #wywołuję quicksorta dla lewej części tablicy
            if pivot_end.next is not b:
                quicksort(pivot_end, b)                      #wywołuję quicksorta dla prawej części tablicy

    def partition(left, right):                              #left jest poprzednikiem pierwszego elementu z lewej w przedziale
        first = left.next                           #firstem będę szedł po kolei po przedziale left->right
        prev = Node()                               #tworzę poprzednika firsta
        prev.next = first
        pivot_start = pivot_end = right                 #początek i koniec pivota domyślnie ustawione na ostatnim elemencie
        last = right                                    #wskaźnik na ostatni element
        greater_than_pvt = Node()                       #wskaźnik na poprzednika podlisty, do której będę przypinał elementy większe od pivota
        greater_pointer = greater_than_pvt              #wskaźnik na wartownika tej podlisty, żebym potem mógł wygodnie ją dopiąć do pivot_end
        ending = last.next                              #tutaj wskaźnik na całą listę która dopięta jest do oryginalnie right'a (potem to przypnę po prostu do nowego lasta)

        while first is not pivot_start:                 #przechodzę firstem po elementach przedziału aż natrafię na start pivota
            if first.value == pivot_end.value:          #dopinanie do przedziału pivotowego
                if prev.value is None:                  #przesunięcie lewej granicy zwracanego przedziału, jeśli przepinam element pierwszy
                    left.next = first.next

                prev.next = first.next                  #odpięcie poprzedników od firsta
                first.next = None                       #standardowa procedura przepinania elementu
                pivot_end.next = first
                pivot_end = first                       #nowym pivot_endem będzie przepięty element
                first = prev.next
            elif first.value > pivot_end.value:         #dopinanie elementów większych od pivota do osobnej podlisty
                if prev.value is None:                  #przepinanie lefta, jeśli first to element pierwszy
                    left.next = first.next

                prev.next = first.next
                first.next = None
                greater_than_pvt.next = first           #dopinam firsta do mojej sublisty elementów większych
                greater_than_pvt = first
                last = first                            #last automatycznie będzie ostatnim elementem greater_than_pvt
                first = prev.next
            else:
                prev = first                            #iteruję dalej po liście
                first = first.next

        if greater_pointer.next:                        #jeśli w ogóle coś jest w podliście z elementami większymi,
            pivot_end.next = greater_pointer.next       #to tutaj dołączam tą sublistę do pivota_enda
        else:
            last = pivot_end                            #jeśli taka lista nie powstała, to ustawiamy lasta na pivot_enda

        last.next = ending                              #dopinam następników mojego oryginalnego przedziału do lasta                                                        #jeśli pivot_start jest lastem, muszę pivot_start przesunąć o jedno w lewp,
        pivot_start = prev                              #bez tego w quicksorcie mi to nie będzie działać bo wpadnie w pętlę nieskończoną

        return left, pivot_start, pivot_end, last       #zwracam wskaźniki na poprzednika lewej części przedziału, na początek, koniec pivota i na koniec przedziału

    def get_last(first):
        while first.next is not None:
            first = first.next
        return first

    new = Node()
    new.next = L
    quicksort(new, get_last(L))
    return new.next

t1 = [randint(1, 10) for _ in range(30)]
t1 = tab2list(t1)
new1 = Node()
new1.next = t1
t = [randint(1, 10000) for _ in range(1000000)]
t = tab2list(t)
start = time()
new = qsort(t)
end = time()
printlist(new)
print(end-start)