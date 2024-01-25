import math

num = float(input("Сумма: "))
while (num / 8) >= 1:
    num = math.trunc(num / 8)
print(num)
