def receipt(list_of_prices):
    theSum = 0
    for i in list_of_prices:
        theSum = theSum + i
    return theSum

list_of_prices = list(map(float, input('Введіть ціни: \n').split()))
list_of_goods= list(map(str, input('Введіть список товарів: \n').split()))
receipt(list_of_prices)
print(receipt(list_of_prices))
print(set(list_of_goods))
