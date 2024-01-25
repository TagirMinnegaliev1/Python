import math

print("Загадайте число от 1 до 1000")
z = 1000/2
x = 1000/2
attempt = 1
while 1:
    print(f"Ваше число {math.trunc(z)}?")
    str = input("Введите >, <  или = : ")
    if str == ">":
        z += x/2
        x /= 2
    elif str == "<":
        z -= x/2
        x/= 2 
    elif str == "=":
        print(f"Ваше число {math.trunc(z)}")
        break
    print(attempt)
    attempt += 1