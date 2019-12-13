print ("Для виходу натисніть N, для продовження Y")
import math
import re
re_numb = re.compile("[-+]?\d+\.?\d?")
re_number = re.compile("\d+$")

def checking(pattern, x):
    return bool(pattern.match(x))

while True:
    print("\n")
    text = input("Ваша відповідь:")
    if text.lower() == "n":
        break
    if text.lower() == "y":

        def val_values1(pattern, values):
            text = input(values)
            while not checking(pattern, text):
                text = input(values)
            return float(text)

        def val_values2(pattern, values):
            text = input(values)
            while not checking(pattern, text):
                text = input(values)
            return int(text)

        def funct(f, a, b, n):
            h = (b - a) / n
            res = (f(a) + f(b)) / 2
            for i in range(1, n):
                res += f(a + i * h)
            res *= h
            print(round(res, 3))


        from math import sin, cos, tan, exp, log
        a = val_values1(re_numb, "Введіть нижню межу інтегрування a = ")
        b = val_values1(re_numb, "Введіть верхню межу інтегрування b = ")
        n = val_values2(re_number, "Введіть кількість частин, на які поділиться графік функції n = ")
        f = lambda x: eval(input('Введіть функцію для інтегрування: '))
        funct(f, a, b, n)


