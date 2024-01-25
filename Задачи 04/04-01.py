import math

days = 0
while 1:
    t = float(input("Введите температуру: "))
    days += 1
    if t > 22:
        print(math.trunc((days - 1) / 7))
        break