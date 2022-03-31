'''Proszę zaimplementować  scalanie dwóch posortowanych list jednokierunkowych do jednej'''

class Node:
  def __init__(self,value=None):
    self.value = value
    self.next = None

  def __str__(self):
    strr = "["
    p = self
    while p is not None:
      strr = strr + str(p.value) + " "
      p = p.next
    strr += "]"
    return strr

def merge(list1, list2):
    result = Node()

    start = result

    while list1!=None and list2!=None:
        if list1.value<list2.value:
            result.next=list1
            list1=list1.next
        else:
            result.next=list2
            list2=list2.next

        result=result.next

    if list1!=None:
        result.next=list1

    if list2!=None:
        result.next=list2

    return start.next


"2.  Algorytm sortowania list jednokierunkowych przez scalanie serii naturalnych"
# tablica na liste
def to_list(t):
  wart = Node(None)
  p = wart
  for i in t:
    p.next = Node(i)
    p = p.next
  return wart.next

def cut_off(first):
    p = first
    q = p.next
    while q is not None:
        if p.value > q.value:
            p.next = None
            return q
        p = q
        q = q.next

    return q

def mergesort(first):
    result = last = Node()

    while True:
        list1 = first
        list2 = cut_off(list1)
        if list2 is None:
            last.next = list1
        first = cut_off(list2)
        if first is None:
            break
        last.next = merge(list1, list2)
        last = getLast(result)






l1 = to_list([1, 2, 3, 4, 1, 2, 3])
print(l1)
l2 = cut_off(l1)
print(l1)
print(l2)


"3'''Mamy daną tablicę A z n liczbami. " \
"Proszę zaproponować algorytm o " \
"złożoności O(n), który stwierdza, czy " \
"istnieje liczba x(tzw. lider A), która występuje w A " \
"na ponad połowie pozycji.'''"


A = [1, 2, 3, 1, 2, 2, 2]

licz = 0

i = 0
for i in range(len(A)):
    if licz == 0:
        licz = 1
        j = i
    elif A[i] == A[j]:
        licz += 1
    else:
        licz -= 1

cnt = 0
for i in range(len(A)):
    if A[i] == A[j]
        cnt += 1
    if cnt > len(A)//2
        print(A[i])
        break

else:
    print("brak")



"4. Zadanie z L litrami wody i pojemnikami i zapełnianiem"


Tab = [((1, 3), (4, 6)), ((2, 8), (5, 9)), ((0, 5), (3, 7))]

def check_if_filled(tank, height):
    if tank[0][0]<height:
