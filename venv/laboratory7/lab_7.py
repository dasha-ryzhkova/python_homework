print("Рижкова Дар'я Олександрівна, КМ-92 \nЛабораторна робота №7 \nВаріант №15 \nЄ текстовий файл. Додати в нього рядок з дванадцяти рисочок (------------), розмістивши його:")
print("після п'ятого рядка;")
print("після останнього з рядків, в яких немає пробілу.")
print("Якщо таких рядків немає, то новий рядок повинен бути доданий після всіх рядків наявного файлу.")
print("В обох випадках результат записати в інший файл.")
print("Для виходу натисніть N, для продовження Y")
import re
import os
re_numb = re.compile("\d+$")
def checking(pattern, x):
    return bool(pattern.match(x))


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


        def file_exist():
            name = input("Введіть шлях до файлу:")
            if os.path.exists(name):
                f = open(name, 'r')
                work_with_file1(f)
            else:
                print("Файл не існує")
                print("Хочете ввести текстовий файл? \n(якщо так натисніть y)")
                text = input("Ваша відповідь:")
                if text.lower() == "y":
                    n = val_values(re_numb, "Введіть кількість рядків n > 6, n = ")
                    if n > 6:
                        f = open('lab.txt', 'w')
                        for i in range(n):
                            pr = input('Введіть рядок: ')
                            f.write(pr + '\n')
                        f.close()
                        f = open('lab.txt', 'r')
                        work_with_file1(f)
                    else:
                        print('n < 6')
                        file_exist()

                if text.lower() == "n":
                    sys.exit()


        def work_with_file1(f):
            rd = f.readlines()
            f.close()
            rd[5] = '------------\n'
            f = open('lab.txt', 'w')
            for el in rd:
                f.write(el)
            f.close()
            f = open('lab.txt', 'r+')
            sym = ' '
            for line in f:
                t = line
                if sym in t:
                    continue
                else:
                    f.write('------------' + '\n')
                    break
            f.close()

            f = open('lab.txt', 'r+')
            file = open('new_file', 'w')
            for ln in f:
                s = ln
                file.write(s)
            f.close()
            file.close()

    file_exist()

