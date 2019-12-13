print ("Рижкова Дар'я Олександрівна, КМ-92 \nЛабораторна робота №6 \nВаріант №15")
print("15) Дан одновимірний масив числових значень, що нараховує n елементів. Дано додатне число t. \nРозділити це число між додатними елементами масиву пропорційно значенням цих елементів і додати отримані частки до відповідних елементів.")
print ("Для виходу натисніть N, для продовження Y")
import re
import random
import math

re_numb = re.compile("\d+$")
re_number = re.compile("[+]?\d+\.?\d?")

def checking(pattern, x):
    return bool(pattern.match(x))

while True:
        print('\n')
        text = input("Ваша відповідь:")
        if text.lower() == "n":
             break
        if text.lower() == "y":
            def val_values1(pattern, values):
                text = input(values)
                while not checking(pattern, text):
                    text = input(values)
                return int(text)

            def val_values2(pattern, values):
                text = input(values)
                while not checking(pattern, text):
                    text = input(values)
                return float(text)

            def create_list(s, n):
                numb_list = random.sample(range(s), n)
                print(numb_list)
                mas(numb_list, t, n - 1)

            def mas(numb_list, t, n):
                res = []
                if n >= 0:
                    result = [round((numb_list[n] + (t * numb_list[n] / sum(numb_list))), 3)]
                    print(*result, sep=', ', end=', ')
                    return mas(numb_list, t, n - 1)
                else:
                    return 1




            s = val_values1(re_numb, "Введіть верхню межу елементів s = ")
            n = val_values1(re_numb, "Введіть кількість елементів n = ")
            t = val_values2(re_number,"Введіть t = ")
            create_list(s, n)
