print ("Рижкова Дар'я Олександрівна, КМ-92 \nЛабораторна робота №4 \nВаріант №15 \n15) Функція - SubWord(s,n,l). Призначення - виділення з рядка s l слів, починаючи зі слова з номером n. ")

def SubWord(s, n, l):
    text = s.split()
    new_text = text[n - 1:n + l - 1]
    new_s = ", ".join(new_text)
    print("Відповідь:", new_s)


def value_n():
    new_s = s.split(" ")
    len_of_s = len(new_s)
    n = val_values(re_numb, "Введіть n = ")
    if len_of_s >= n:
        value_l(n)
    else:
        print("Ви ввели завелике n.")
        return value_n()

def value_l(n):
    new_s = s.split(" ")
    len_of_s = len(new_s)
    l = val_values(re_numb, "Введіть l = ")
    if len_of_s-n >= l-1:
        SubWord(s, n, l)
    else:
        print("Ви ввели завелике l.")
        return value_l(n)

print ("Для виходу натисніть N, для продовження Y")
import re
re_numb = re.compile("\d+$")
def checking(pattern, rect_side):
    return bool(pattern.match(rect_side))
while True:
        text = input("Ваша відповідь:")
        if text.lower() == "n":
             break
        if text.lower() == "y":
            def val_values(pattern, values):
                text = input(values)
                while not checking(pattern, text):
                    text = input(values)
                return int(text)

            s = input("Введіть s = ")
            value_n()
