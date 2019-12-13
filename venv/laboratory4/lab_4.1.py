print ("Рижкова Дар'я Олександрівна, КМ-92 \nЛабораторна робота №4 \nВаріант №15 \n15) Два прямокутники задати парами чисел (a1, b1) і (a2, b2), що визначають довжини їх сторін. Написати функцію, яка з'ясовує, чи можна один з прямокутників цілком помістити в іншому. Передбачається таке розташування прямокутників, при якому зберігається паралельність сторін. ")
print ("Для виходу натисніть N, для продовження Y")
import re
re_numb = re.compile("\d+[.\d+]{0,1}$")
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
                return text

            rect_side_a1 = val_values(re_numb, "Введіть сторону прямокутника а1 = ")
            rect_side_a2 = val_values(re_numb, "Введіть сторону прямокутника а2 = ")
            rect_side_b1 = val_values(re_numb, "Введіть сторону прямокутника b1 = ")
            rect_side_b2 = val_values(re_numb,"Введіть сторону прямокутника b2 = ")
            def a_1_bigger():
                if rect_side_b1 > rect_side_b2 :
                    print("Другий прямокутник вміщується в перший.")
                elif rect_side_b2 > rect_side_b1:
                    print("Ні перший прямокутник не вміщується в другий, ні другий - в перший.")
                else:
                    print("Другий прямокутник вміщується в перший.")
            def a_2_bigger():
                if rect_side_b2 > rect_side_b1 :
                    print("Перший прямокутник вміщується в другий.")
                elif rect_side_b1 > rect_side_b2:
                    print("Ні перший прямокутник не вміщується в другий, ні другий - в перший.")
                else:
                    print("Перший прямокутник вміщується в другий.")
            def eqval():
                if rect_side_b1 == rect_side_b2:
                    print("Прямокутники співпадають.")
                elif rect_side_b1 > rect_side_b2 :
                    print("Другий прямокутник вміщується в перший.")
                else:
                    print("Перший прямокутник вміщується в другий.")
            def solut():
                if rect_side_a1 > rect_side_a2:
                    a_1_bigger()
                elif rect_side_a1 < rect_side_a2:
                    a_2_bigger()
                else:
                    eqval()
            solut()
