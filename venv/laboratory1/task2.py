import re
re_numb = re.compile("\d+$")


def checking(pattern, x):
    return bool(pattern.match(x))


def val_values(pattern, values):
    text = input(values)
    while not checking(pattern, text):
        text = input(values)
    return int(text)


n = val_values(re_numb, "Введіть n = ")


def age(n):

    """
      Написати програму, яка аналізує дані про вік і відносить людину до однієї з чотирьох груп: дошкільник, учень, працівник, пенсіонер. Вік вводиться з клавіатури.
    :param n:int, вводить користувач, ціле число.
    :return:str, слово.
    """

    if (0 <= n <= 6):
        print("Дошкільник")
    elif (6 < n <= 17):
        print("Учень")
    elif (17 < n <= 65):
        print("Працівник")
    elif (n > 65) :
        print("Пенсіонер")
    else:
        print("Помилка, неправильні дані")


age(n)