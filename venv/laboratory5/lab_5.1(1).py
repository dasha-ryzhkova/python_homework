print ("Рижкова Дар'я Олександрівна, КМ-92 \nЛабораторна робота №5 \nВаріант №15 \n15) 15) Створити три списки (W, X, Y). Необхідно: знайти у списку W елементи, наявні у списку X і замінити їх відповідними елементами списку Y, інші елементи залишити без зміни.")
print ("Для виходу натисніть N, для продовження Y")
while True:
        text = input("Ваша відповідь:")
        if text.lower() == "n":
             break


        def val():
            y = list(map(str, input(
                'Введіть другий список(довжина другого має бути така сама, як і довжина першого): \n').split()))
            check(y)


        def check(y):
            if len(x) == len(y):
                w = list(map(str, input('Введіть третій список: \n').split()))
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
                    if elem == x[i]:
                        ordered.append(y[i])
                    if not isinstance(elem, list):
                        if elem not in x:
                            ordered.append(elem)
            result(ordered)


        x = list(map(str, input('Введіть перший список: \n').split()))
        val()

# x = a c v j
# y = 1 2 3
# w = a x v j c i p d