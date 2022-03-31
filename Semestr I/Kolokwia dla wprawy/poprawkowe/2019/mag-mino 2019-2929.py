"""
2. W grze mag-mino wykorzystuje się klocki, które mają kształt prostokątów, na których obydwu końcach znajduje
się liczba oczek od 0 do 9. Na każdym klocku z dwóch jego końców liczba oczek jest inna. W komplecie liczącym 90
klocków do gry występują wszystkie kombinacje oczek i każda kombinacja występuje dokładnie jeden raz. Proszę
napisać funkcję, która dla danego zbioru N klocków wyznacza najdłuższy ciąg jaki można z nich ułożyć.
Na przykład dla zbioru 8 klocków: [2|8] [0|1] [2|3] [3|6] [2|6] [2|9] [3|4] [6|7]
najdłuższy ciąg jaki można ułożyć ma długość 5 i ma postać : [8|2] [2|3] [3|6] [6|2] [2|9]
Dane opisujące zestaw:
const int N= …
struct klocek {
 int a;
 int b; // b>a
};
klocek zestaw[N];
Do funkcji należy przekazać zestaw klocków, funkcja powinna zwrócić największą długość ciągu jaki można z tego
zestawu zbudować. Wskazówka : kiedy z zestawu klocków da się zbudować ciąg?
"""

def longest_possible(klocek):
    tab_of_first = [-1]*len(klocek)
    tab_of_second = [-1] * len(klocek)
    i = 0
    for x in klocek:
        tab_of_first[i] = x[0]
        tab_of_second[i] = x[i]

    for x in range(10):
        count = 0
        for y in range(len(klocek)):
            if tab_of_first[y] == x:
                count += 1
            if tab_of_second[y] == x:
                count += 1




def solve_it(klocek):

    def sort_klocki(tab):
        new = [0]*len(tab)


    def reverse(x):
        new = [0, 0]
        new[0] = x[1]
        new[1] = x[0]
        return new

    def check_if_works(tab):
        for x in range(len(tab)-1):
            if tab[x][1] != tab[x+1][0]:
                return False

        return True

    result = 1
    check = False
    winning_tab = []
    tab_of_all = []
    def rekur(klocek, tab, tab_of_forbidden, i):
        nonlocal tab_of_all
        if tab in tab_of_all:
            return
        tab_of_all.append(tab)
        if i > 1 and not check_if_works(tab):
            return
        print(tab, i)
        nonlocal result, check, winning_tab
        if len(tab) > result:
            result = len(tab)
            winning_tab = tab
            #check = True
        tab = tab[:]
        tab_of_forbidden = tab_of_forbidden[:]

        for x in range(len(klocek)):
            #
            #if check:
                #return
            if x not in tab_of_forbidden:
                rekur(klocek,[klocek[x]]+tab, tab_of_forbidden+[x], i+1)
                rekur(klocek,  tab + [klocek[x]], tab_of_forbidden + [x], i+1)
                a = reverse(klocek[x])
                rekur(klocek, [a] + tab, tab_of_forbidden + [x], i+1)
                rekur(klocek, tab + [a], tab_of_forbidden + [x], i+1)

    for x in range(len(klocek)):
        rekur(klocek, [klocek[x]], [x], 1)


    return result, winning_tab




#[2,8], [0,1], [2,3], [3,6], [2,6], [2,9], [3,4], [6,7]
# [2,9], [3,6], [8,2], [2,3], [6,2], [4, 5], [7,1], [8, 9], [0, 1], [3, 5]

klocek = [[2,9], [3,6], [8,2], [2,3], [6,2], [4, 5], [7,1], [8, 9], [0, 1], [3, 5]]


print(solve_it(klocek))
