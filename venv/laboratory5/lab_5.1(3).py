print ("Рижкова Дар'я Олександрівна, КМ-92 \nЛабораторна робота №5 \nВаріант №15 \n15) Створити три списки (W, X, Y). Необхідно: знайти у списку W елементи, наявні у списку X і замінити їх відповідними елементами списку Y, інші елементи залишити без зміни.")
print ("Для виходу натисніть N, для продовження Y")
import re
re_numb = re.compile("\d+$")
def checking(pattern, x):
    return bool(pattern.match(x))
while True:
    text = input("Ваша відповідь:")
    if text.lower() == "n":
        break
    def val_values(pattern, values):
        text = input(values)
        while not checking(pattern, text):
            text = input(values)
        return int(text)


    def val():
        y = list(map(str, input('Введіть другий список(довжина другого має бути така сама, як і довжина першого): \n').split()))
        check(y)


    def check(y):
        if len(x) == len(y):
            n = val_values(re_numb, "Введіть n = ")
            w = []
            for l in range(n):
                w.append(list(map(str, input('Введіть третій список: \n').split())))
            listfunct(x, y, w)
        else:
            print('Помилка, не правильна довжина списка.')
            return val()


    def result(ordered):
        new_list = []
        for e in ordered:
            if e not in new_list:
                new_list.append(e)
        print(new_list)


    def listfunct(x, y, w):
        ordered = []
        for elem in w:
            for i in range(len(x)):
                if isinstance(elem, list):
                    listinlist(elem, y, ordered)
        result(ordered)


    def listinlist(elem, y, ordered):
        list_of_elem = []
        for this_elem in elem:
            for j in range(len(elem)):
                if this_elem == x[j]:
                    list_of_elem.append(y[j])
                if this_elem not in x:
                    list_of_elem.append(this_elem)
        res(list_of_elem, ordered)


    def res(list_of_elem, ordered):
        new_list_for_elem = []
        for e in list_of_elem:
            if e not in new_list_for_elem:
                new_list_for_elem.append(e)
        ordered.append(new_list_for_elem)


    x = list(map(str, input('Введіть перший список: \n').split()))
    val()


# x = a c v j
# y = 1 2 3
# w = a x v j
#     c i p d
#     c v d a