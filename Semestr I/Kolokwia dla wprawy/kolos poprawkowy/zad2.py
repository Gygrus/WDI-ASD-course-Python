
def check_count(word):
    lett = ['a', 'e', 'i', 'o', 'u', 'y']
    counter = 0
    for x in lett:
        counter += word.count(x)
    return counter

def func(word):
    counter = 0
    def rekur(word, current, tab, i):
        if i == len(word) - 1:
            if check_count(current) == 1:
                nonlocal counter
                tab = list(tab)
                tab.append(current)
                tab = tuple(tab)
                print("-".join(tab))
                counter += 1
        else:
            if check_count(current) <= 1:
                rekur(word, current + word[i+1], tab, i+1)

            if check_count(current) == 1:
                tab = list(tab)
                tab.append(current)
                tab = tuple(tab)
                rekur(word, word[i+1], tab, i+1)

    rekur(word, word[0], tuple(), 0)
    return counter


print(func('informatyka'))
print(check_count('’sesja'))