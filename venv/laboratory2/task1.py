import re
import math
re_numb = re.compile("[-+]?\d+\.?\d?")
re_number = re.compile("\d+$")


def checking(pattern, x):
    return bool(pattern.match(x))


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

def sigma():

    """
     Організація циклу за допомогою оператора for.
    :return:float, виведення суми у порядку обчислення.
    """

    for i in range(0, bound_of_sum + 1):
        y = math.sqrt(x ** 2 + 1)
        sum = (i + 1) / y
        print("Сума=", round(sum, 3))


x = val_values1(re_numb, "Введіть x = ")
bound_of_sum = val_values2(re_number, "Введіть верхню межу суми n = ")
sigma()