print ("Рижкова Дар'я Олександрівна, КМ-92 \nЛабораторна робота №5 \nВаріант №15 \n15) Створити три списки (W, X, Y). Необхідно: знайти у списку W елементи, наявні у списку X і замінити їх відповідними елементами списку Y, інші елементи залишити без зміни.")
def listfunct(x, y, w):
    ordered = []
    for elem in w:
        for i in range(len(x)):
            if isinstance(elem, list):
                listinlist(elem, ordered)
            if elem == x[i]:
                ordered.append(y[i])
            if not isinstance(elem, list):
                if elem not in x:
                    ordered.append(elem)
    result(ordered)


def listinlist(elem, ordered):
    list_of_elem = []
    for this_elem in elem:
        for j in range(len(elem)):
            if this_elem == x[j]:
                list_of_elem.append(y[j])
            elif this_elem not in x:
                list_of_elem.append(this_elem)
            else:
                continue
        res(list_of_elem, ordered)


def res(list_of_elem, ordered):
    new_list_for_elem = []
    for e in list_of_elem:
        if e not in new_list_for_elem:
            new_list_for_elem.append(e)
    ordered.append(new_list_for_elem)


def result(ordered):
    new_list = []
    for e in ordered:
        if e not in new_list:
            new_list.append(e)
    print(new_list)


x = ['a', 'b', 'c']
y = [1, 2, 3]
w = [['a'], 'a', 'c', 'f',  ['d'], ['a', 'b']]

listfunct(x, y, w)

