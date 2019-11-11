import re
re_numb = re.compile("\d+$")


def checking(pattern, x):
    return bool(pattern.match(x))


def val_values(pattern, values):
    text = input(values)
    while not checking(pattern, text):
        text = input(values)
    return int(text)

def factorials():

    """
     Дано ціле число N(>0). Знайти подвійний факторіал N: N!!= N•(N-2) •(N-4)• ... (останній співмножник дорівнює 2, якщо N - парне, і 1, якщо N - непарне).
    :return:int, факторіали у порядку обчислення
    """

    if (n % 2):
        num = 1
        for i in range(num + 2, n + 1, 2):
            num *= i
            print("N!!=" + (str(num)))
    else:
        num = 2
        for i in range(num + 2, n + 1, 2):
            num *= i
            print("N!!=" + (str(num)))


n = val_values(re_numb, "Введіть n = ")
factorials()