import re

re_numb = re.compile("[1, 2]{1}$")


def checking(pattern, x):
    return bool(pattern.match(x))


def val_values(pattern, values):
    text = input(values)
    while not checking(pattern, text):
        text = input(values)
    return int(text)


def sortsym():

    """
    Упорядкувати символи в рядку за алфавітом.
    :return:list, ортований список.
    """

    if n == 1 :
        new_list = sorted(sym, reverse = False)
        print(new_list)
    if n == 2:
        new_list = sorted(sym, reverse = True)
        print(new_list)


text = input("Введіть текст: \n")
n = val_values(re_numb, "Введіть n = 1 для прямого сортування або n = 2 для зворотнього \nn = ")
sym = list(text)
sortsym()