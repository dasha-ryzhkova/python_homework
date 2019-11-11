"""Потрібно обчислити, скільки банок фарби потрібно, щоб пофарбувати поверхню бака циліндричної форми.
Пофарбувати треба і зовні, і зсередини.
Користувач вводить діаметр і висоту бака, а також, яку площу можна забарвити однієї банкою фарби."""

import re
import math

re_numb = re.compile("[+]?\d+\.?\d?")

def checking(pattern, x):
    return bool(pattern.match(x))


def checking(pattern, x):
    return bool(pattern.match(x))


def val_values(pattern, values):
    text = input(values)
    while not checking(pattern, text):
        text = input(values)
    return float(text)


h = val_values(re_numb, "Введіть h = ")
d = val_values(re_numb, "Введіть d = ")
n = val_values(re_numb, "Введіть n = ")


#N = math.ceil(3.14 * d * (4 * h + d) / (2 * n))

print("Кількість банок з фарбою ", math.ceil(3.14 * d * (4 * h + d) / (2 * n)))