import math

num = int(input("Введите целое неотрицательное число: "))
try:
     print(math.factorial(num))
except ValueError:
    print("Число должно быть неотрицательным!")