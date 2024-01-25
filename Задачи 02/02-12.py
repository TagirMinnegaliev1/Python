import math

str = input("Введите сообщенение: ")
price = len(str) * 40 
if price > 100:
    rub = math.trunc(price / 100)
    kop = price - (rub * 100)
    print(f"{rub} р. {kop} к.")
else:
    print(f"{price} к.")
