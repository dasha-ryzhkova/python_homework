print ("Рижкова Дар'я Олександрівна, КМ-92 \nЛабораторна робота №5 \nВаріант №15 \n15) Завдання на множині: \nА={1 ,a, ee, ww, c, d} \nB={4, a, b, tt, 1, 3} \nЗнайти: \nF=((A\B)\(A\B`))")
import itertools
def setoper():
    x = a.union(b)
    un(x)
    print("б)Перетин двох множин: C = ", a & b)
    print("в)Різниця першої і другої множин:  C = ", a.difference(b))
    print("г)Різниця другої і першої множин: C = ", b.difference(a))
    print("д)Симетрична різниця двох множин: C = ", a.symmetric_difference(b))
    print("е)Доповнення першої множини: C = ", u.difference(a))
    print("є)Доповнення другої множини:  C = ", u.difference(b))
    print("и) F = ", (a - b) & (a | b))
    print('Декартові добутки:\n')
    print('ж) А*В = ')
    for i in itertools.product(a, b):
        print('   ', i)
    print("з) В*А = ")
    for j in itertools.product(b, a):
        print('   ', j)



def un(x):
    if x == u:
        print("a)Об'єднання двох множин: C = U")
    else:
        print("a)Об'єднання двох множин: C = ", x)





a = {1, 'a', 'ee', 'ww', 'c', 'd'}
b = {4, 'a', 'b', 'tt', 1, 3}
u = {1, 2, 3, 4, 'a', 'b', 'c', 'd', 'ee', 'tt', 'ww'}
setoper()

