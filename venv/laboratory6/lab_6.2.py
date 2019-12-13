print ("Рижкова Дар'я Олександрівна, КМ-92 \nЛабораторна робота №6 \nВаріант №15")
print("15) Виконати обробку елементів прямокутної матриці A, що має n рядків і m стовпців. Всі елементи мають цілий тип. Дано ціле число h. Визначити, які стовпці мають хоча б одне таке число, а які не мають.")
print ("Для виходу натисніть N, для продовження Y")
import re
import random
import numpy as np
import math

re_numb = re.compile("\d+$")

def checking(pattern, x):
    return bool(pattern.match(x))

while True:
    print("\n")
    text = input("Ваша відповідь:")
    if text.lower() == "n":
        break
    if text.lower() == "y":
        def val_values(pattern, values):
            text = input(values)
            while not checking(pattern, text):
                text = input(values)
            return int(text)

        def val_k(p):
            k = val_values(re_numb, "Введіть максимум значень елементів матриці k, k > p, k = ")
            if k > p:
                val_h(p, k)
            else:
                print("Помилка,k не задовільняє умову k > p.")
                val_k(p)

        def val_h(p, k):
            h = val_values(re_numb, "Введіть h, p <= h <= k, h = ")
            if p <= h <= k:
                create_matr(p, k, m, n, h)
            else:
                print("Помилка,h не задовільняє умову p <= h <= k.")
                val_h(p, k)

        def create_matr(p, k, m, n, h):
            a = np.random.randint(p, k + 1, (m, n))
            print(a)
            change_matr(a, m, n, h)

        def change_matr(a, m, n, h):
            print("Номер(a) стовпчика(iв), що містить h:")
            for i in range(m):
                for j in range(n):
                    if a[i][j] == h:
                        print(j + 1, end= '  ')


        m = val_values(re_numb, "Введіть кількість рядків матриці А, m = ")
        n = val_values(re_numb, "Введіть кількість стовпців матриці А, n = ")
        p = val_values(re_numb, "Введіть мінімум значень елементів матриці p = ")
        val_k(p)


