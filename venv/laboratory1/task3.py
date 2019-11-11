import re
re_numb = re.compile("[-+]?\d+\.?\d?")


def checking(pattern, x):
    return bool(pattern.match(x))


def val_values(pattern, values):
     text = input(values)
     while not checking(pattern, text):
         text = input(values)
     return float(text)


def y(x):

    """
    Обчислення конкретної функції, в залежності від введеного значення х.
    :param x: float, вводить користувач, число.
    :return: float, число.
    """

    if x <= 3.6:
        result = 5*x/(10*x**2+1)
        print("F(x)= " +str(round(result, 3)))
    else:
        result = 45*x**2 + 3
        print("F(x)= " +str(round(result, 3)))


x = val_values(re_numb, "Введіть x = ")
y(x)