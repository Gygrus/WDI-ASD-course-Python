# Piotr Socała
from queue import PriorityQueue
from random import randint

# pomocnicza klasa Huf_sign, dzięki której
# łatwiej zyskamy strukturę drzewa
class Huf_sign:
    def __init__(self, val, symbol, left=None, right=None):
        # val to wartość wierzchołka w drzewie
        # (na początku częstość występowania znaku w napisie)
        self.val = val
        # left i right jako oznaczenie lewego i prawego dziecka
        # danego wierzchołka
        self.left = left
        self.right = right
        # przypisany kod dla podanego znaku
        self.print = ""
        # przydatny przy wypisywaniu, żeby wwypisać
        # również odpowiedni symbol przed kodem
        self.symbol = symbol

    # to pozwala na uniknięcie błędu spowodowanego
    # porównywaniem dwóch obiektów klasy Huf_sign
    # w PriorityQueue zamiast ich wartości, w przypadku
    # kiedy ich wartości są te same
    def __gt__(self, other):
        return 0



def huffman(S, F):
    # funkcja do przypisania odpowiednim znakom ich kodu
    def get_solution(curr_digit, curr_node, counter):
        # jeśli nasz obiekt nie ma potomka, to oznacza
        # że jest on początkowym obiektem i należy przypisać
        # mu (w metodzie .print) znaleziony kod
        # do result dodajemy iloczyn jego wystąpień i długości kodu
        if curr_node.left is None:
            nonlocal result
            curr_node.print += curr_digit
            result += counter*curr_node.val
            return

        # jeśli węzeł ma swoje dzieci, schodzimy po drzewie dalej,
        # węzły o wartości mniejszej (prawe dzieci) dostają "1",
        # te o większej wartości (lewe dzieci) dostają "0"
        else:
            get_solution(curr_digit+"0", curr_node.left, counter + 1)
            get_solution(curr_digit+"1", curr_node.right, counter + 1)

    # przypisuję długość tablicy S jako ilość początkowych liści drzewa
    # zamieniam je na obiekty klasy Huf_sign
    n = len(S)
    for x in range(n):
        S[x] = (Huf_sign(F[x], S[x]))

    # inicjalizuję kolejkę priorytetową, z której będę
    # wyciągał węzły o najmniejszych wartościach
    min_item = PriorityQueue()
    for x in range(n):
        min_item.put((S[x].val, S[x]))

    # pętla w której tworzę drzewo
    while True:
        # przypisuje dwa obiekty o najmniejszej wartości jako
        # dzieci obiektu parent o wartości równej sumie wartości dzieci
        x = min_item.get()
        y = min_item.get()
        parent = Huf_sign(x[1].val + y[1].val, 0, y[1], x[1])
        # jeśli to były dwa ostatnie elementy kolejki to wychodzę
        # z pętli
        if min_item.empty():
            break
        # dodawanie ojca do kolejki
        min_item.put((parent.val, parent))

    # new jako ostatni wierzchołek drzewa
    new = parent
    # result jako zwracana liczba bitów
    result = 0
    # uzupełnianie początkowych obiektów Huf_sign
    # ich kodami za pomocą get_solution
    get_solution("", new, 0)

    # wypisanie wyniku
    for x in range(n):
        print(S[x].symbol, ":", S[x].print)

    print(result)

S = ["a", "b", "c" ,"d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]
F = [randint(1, 1000) for _ in range(16)]
print(F)
huffman(S, F)